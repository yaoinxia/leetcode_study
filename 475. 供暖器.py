class Solution:
    def findRadius(self, houses=[1,5], heaters=[1, 5, 6]):
        # 定义所可以覆盖的最小半径

        if len(heaters) >= len(houses) and houses == heaters[:len(houses)]:
            return 0
        # 判断heaters是否为1
        if len(heaters) == 1:
            min_radius = max(abs(heaters[0]-houses[0]), abs(houses[-1]-heaters[0]))
            return min_radius
        min_radius = max(abs(heaters[0]-houses[0]), abs(houses[-1]-heaters[-1]))
        i = 0
        while i < len(heaters)-1:
            if heaters[i+1]- heaters[i] > min_radius:
                min_radius = heaters[i+1]- heaters[i]
            i += 1
        # [1, 2, 3, 4, 5]
        return min_radius//2

    def findRadius2(self, houses=[1,2, 5], heaters=[7]):
        # 定义所可以覆盖的最小半径
        min_len = []
        for i in range(len(houses)):
            sub_min = abs(houses[i] - heaters[0])
            for j in range(len(heaters)):
                if abs(houses[i] - heaters[j]) < sub_min:
                    sub_min = abs(houses[i] - heaters[j])
            min_len.append(sub_min)
        # print(min_len)
        # print(max(min_len))
        rad = max(min_len)
        return rad

    def findRadius3(self, houses=[1, 2, 5], heaters=[1, 3, 4, 7]):
        result = []
        # 特殊情况，只有一个加热器。
        if len(heaters) == 1:
            for item in houses:
                result.append(abs(item - heaters[0]))
            return max(result)

        houses.sort()  # 进行排序。
        heaters.sort()
        pin1 = 0  # 指向房屋的前一个加热器
        pin2 = 1  # 指向房屋的后一个加热器

        for house in houses:
            while pin2 < len(heaters) - 1 and heaters[pin2] < house:
                pin2 += 1
                pin1 += 1
            # 取房屋与前后加热器的最小距离
            result.append(min(abs(house - heaters[pin1]), abs(heaters[pin2] - house)))
        return max(result)  # 返回结果最大值

    def findRadius3(self, houses=[1, 2, 5], heaters=[1, 3, 4, 7]):
        result = []
        if len(heaters) == 1:
            for h in houses:
                result.append(abs(h-heaters[0]))
            return max(result)
        houses.sort()
        heaters.sort()
        left = 0
        right = 1
        # 房屋只有前面有取暖器，或者只有后面有
        for h in houses:
            # 如果房屋在取暖器右边或者在取暖器左边
            if h < heaters[left]:
                result.append(min(abs()))

    def findRadius3(self, houses=[1, 2, 5], heaters=[3, 4, 7]):
        result = []
        houses.sort()
        heaters.sort()
        min_r = 0
        if houses[0] >= heaters[-1]:
            return houses[-1] - heaters[-1]
        if houses[-1] <= heaters[0]:
            return heaters[0] - houses[0]
        for ho in houses:
            for i, he in enumerate(heaters):
                if i + 1 < len(heaters):
                    if ho <= he and ho <= heaters[i+1]:
                        result.append(he-ho)
                        break
                    elif  ho >= he and ho >= heaters[i+1]:
                        result.append(ho-he)
                        break
                    elif ho >= he and ho <= heaters[i+1]:
                        result.append(min(abs(ho-he), abs(heaters[i+1]-ho)))
                        break
        print(result)
        return max(result)

        # 房屋有前有后的情况

if __name__ == '__main__':
    print(Solution().findRadius3())






        # 定位heaters之间差距最大的点

