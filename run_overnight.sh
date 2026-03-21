#!/bin/bash
# Overnight pipeline runner — drafts ch_04 through ch_18

PYTHON=~/Documents/GitHub/autonovel/.venv/bin/python3
DIR=~/Documents/GitHub/autonovel
LOG=/tmp/overnight_pipeline.log

cd $DIR

echo "[$(date)] Starting overnight pipeline — ch_04 to ch_18" >> $LOG

for N in 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18; do
    # Skip if already exists
    if [ -f "chapters/ch_$(printf '%02d' $N).md" ]; then
        echo "[$(date)] ch_$N already exists, skipping" >> $LOG
        continue
    fi

    echo "[$(date)] Drafting chapter $N..." >> $LOG
    ATTEMPTS=0
    SUCCESS=0

    while [ $ATTEMPTS -lt 3 ] && [ $SUCCESS -eq 0 ]; do
        ATTEMPTS=$((ATTEMPTS + 1))
        $PYTHON draft_chapter.py $N >> $LOG 2>&1
        EXIT=$?

        if [ $EXIT -eq 0 ] && [ -f "chapters/ch_$(printf '%02d' $N).md" ]; then
            echo "[$(date)] ch_$N drafted OK (attempt $ATTEMPTS)" >> $LOG

            # Evaluate
            echo "[$(date)] Evaluating ch_$N..." >> $LOG
            $PYTHON evaluate.py --chapter=$N >> $LOG 2>&1

            # Extract score
            SCORE=$(grep "overall_score:" $LOG | tail -1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
            echo "[$(date)] ch_$N score: $SCORE" >> $LOG

            # Check if score >= 6.0
            PASS=$(python3 -c "print('yes' if float('${SCORE:-0}') >= 6.0 else 'no')" 2>/dev/null)
            if [ "$PASS" = "yes" ]; then
                git add chapters/ch_$(printf '%02d' $N).md && git commit -m "ch_$(printf '%02d' $N): drafted, score $SCORE"
                echo "[$(date)] ch_$N committed" >> $LOG
                SUCCESS=1
            else
                echo "[$(date)] ch_$N score $SCORE < 6.0, retrying..." >> $LOG
                rm -f chapters/ch_$(printf '%02d' $N).md
            fi
        else
            echo "[$(date)] ch_$N draft failed (attempt $ATTEMPTS, exit $EXIT)" >> $LOG
        fi
    done

    if [ $SUCCESS -eq 0 ]; then
        echo "[$(date)] ch_$N SKIPPED after 3 failed attempts" >> $LOG
    fi
done

echo "[$(date)] All chapters done. Running full eval..." >> $LOG
$PYTHON evaluate.py --full >> $LOG 2>&1

git add -A && git commit -m "pipeline: overnight draft complete" >> $LOG 2>&1

echo "[$(date)] PIPELINE COMPLETE" >> $LOG
