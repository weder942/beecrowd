package main

import "fmt"

func main() {
	var num1, num2, produto int
	fmt.Scanf("%d", &num1)
	fmt.Scanf("%d", &num2)
	produto = num1 * num2
	fmt.Printf("PROD = %d\n", produto)
}
