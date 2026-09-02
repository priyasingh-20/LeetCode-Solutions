class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2

        Lsum = 0
        Rsum = 0
        QLcount = 0
        QRcount = 0

        for i in range(n):
            if num[i] == "?":
                QLcount += 1
            else:
                Lsum += int(num[i])

            if num[i + n] == "?":
                QRcount += 1
            else:
                Rsum += int(num[i + n])

        diff = Rsum - Lsum
        Qdiff = QLcount - QRcount

        return 2 * diff != 9 * Qdiff