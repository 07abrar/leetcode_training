class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        money_at_hand = []
        for bill in bills:
            if bill != 5 and 5 not in money_at_hand:
                return False
            elif bill == 20 and not (
                money_at_hand.count(5) >= 3 or
                ((money_at_hand.count(10) >= 1 and money_at_hand.count(5) >= 1))
            ):
                return False
            if bill == 10:
                money_at_hand.remove(5)
            elif bill == 20:
                if 10 in money_at_hand:
                    money_at_hand.remove(10)
                    money_at_hand.remove(5)
                else:
                    for _ in range(3):
                        money_at_hand.remove(5)
            money_at_hand.append(bill)
        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    solution = Solution()
    print(solution.lemonadeChange(bills))

    bills = [5, 5, 10, 10, 20]
    solution = Solution()
    print(solution.lemonadeChange(bills))
