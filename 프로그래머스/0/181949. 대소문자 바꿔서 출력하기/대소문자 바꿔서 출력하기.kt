fun main(args: Array<String>) {
val s1 = readLine()!!
for (str in s1.toCharArray()) {
    if (str.isUpperCase()) {
        print(str.toLowerCase())
    } else {
        print(str.toUpperCase())
    }
}
}