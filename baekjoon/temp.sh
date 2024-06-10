#!/bin/bash

# 숫자를 저장할 파일명
file="number.txt"

# 파일이 존재하지 않으면 0을 씁니다.
if [ ! -f "$file" ]; then
  echo 0 > "$file"
fi

# 파일에서 숫자를 읽습니다.
number=$(cat "$file")

# 숫자에 1을 더합니다.
incremented_number=$((number + 1))

# 결과를 파일에 다시 씁니다.
echo $incremented_number > "$file"

echo "The number has been incremented to: $incremented_number"
