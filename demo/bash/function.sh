#!/usr/bin/env bash

sayHello(){
  echo "Hello!"
  return 5
}
# echo "11: $?"
sayHello
# echo "22: $?"
# echo "22-: $?"
# echo '---'
# echo "22--5: $?"

funWithReturn(){
    # echo "33: $?"
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
# echo "44: $?"
funWithReturn
echo "输入的两个数字之和为 $? !"

# 参数
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73

read -p "\n wait a minute" n
