func compareTriplets(a: [Int], b: [Int]) -> [Int] {
    var count = [0,0]
    for i in 0...(a.count - 1) {
        if a[i] > b[i] {
            count[0] += 1
        }
        else if a[i] < b[i] {
            count[1] += 1
        }
    }
    return count
}
