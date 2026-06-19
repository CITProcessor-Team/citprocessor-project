#!/bin/bash

CONFIG_FILE="pipeline.conf"
REPORT_FILE="report.html"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: $CONFIG_FILE not found."
    exit 1
fi

# Start HTML report
cat > "$REPORT_FILE" <<EOF
<html>
<head>
<title>CI Pipeline Report</title>
<style>
table {
    border-collapse: collapse;
    width: 80%;
}
th, td {
    border: 1px solid black;
    padding: 8px;
    text-align: center;
}
.pass {
    background-color: lightgreen;
}
.fail {
    background-color: salmon;
}
.skip {
    background-color: lightgray;
}
</style>
</head>
<body>

<h2>CI Pipeline Report</h2>

<table>
<tr>
<th>Step</th>
<th>Command</th>
<th>Status</th>
<th>Execution Time (ms)</th>
</tr>
EOF

pipeline_failed=0

while read -r line
do
    [ -z "$line" ] && continue

    IFS=':' read -r name cmd <<< "$line"

    if [ "$pipeline_failed" -eq 1 ]; then
        echo "<tr><td>$name</td><td>$cmd</td><td class=\"skip\">SKIPPED</td><td>-</td></tr>" >> "$REPORT_FILE"
        continue
    fi

    echo "Running: $name"

    START=$(date +%s%N)

    bash -c "$cmd"
    status=$?

    END=$(date +%s%N)

    duration=$(( (END - START) / 1000000 ))

    if [ $status -eq 0 ]; then
        result="PASS"
        color="pass"
    else
        result="FAIL"
        color="fail"
        pipeline_failed=1
    fi

    echo "<tr><td>$name</td><td>$cmd</td><td class=\"$color\">$result</td><td>$duration</td></tr>" >> "$REPORT_FILE"

done < "$CONFIG_FILE"

cat >> "$REPORT_FILE" <<EOF
</table>

</body>
</html>
EOF

echo "Pipeline complete."
echo "HTML report generated: $REPORT_FILE"
