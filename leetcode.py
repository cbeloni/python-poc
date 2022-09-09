from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_to_index = [(num, index) for index, num in enumerate(nums)]
        num_to_index.sort()
        
        left, right = 0, len(nums) - 1
        
        while (left < right):
            if num_to_index[left][0] + num_to_index[right][0] == target:
                return [num_to_index[left][1], num_to_index[right][1]]
            elif num_to_index[left][0] + num_to_index[right][0] < target:
                left += 1
            else:
                right -= 1
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}
        
        for i in range(len(nums)):
            if target - nums[i] in mapping:
                return [i, mapping[target - nums[i]]]
            mapping[nums[i]] = i  
                        
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x)[::-1] == str(x):
            return True
        
    def romanToInt(self, s: str) -> int:
        mapa = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        numero_invertido = s[::-1]
        resultado = 0
        numero_anterior = 0
        for i in numero_invertido:
            print (i)
            if numero_anterior > mapa[i]:
                resultado -= mapa[i]
                continue
            resultado += mapa[i]
            numero_anterior = mapa[i]
        
        return resultado

    def longest_common_prefix(self, strs: List[str]) -> str:
        def maior_string(strs: List[str]):
            strs_com_tamanho = {}
            for i in strs:
                strs_com_tamanho[i] = len(i)
            return sorted(strs_com_tamanho, reverse=True)[0]

        len_string = maior_string(strs)
        strs.remove(len_string)
        print(strs)
        prefixo = ""
        for i in range(len(len_string)):
            for s in strs:
                if s == "":
                    return prefixo
                try:
                    if len_string[i] not in s[i]:
                        return prefixo
                except:
                    return prefixo

            prefixo += len_string[i]
        return prefixo

        def longestCommonPrefix2(self, strs: List[str]) -> str:
            l = []
            for i in zip(*strs):
                if (len(set(i))) > 1:
                    break
                l.append(i[0])
            return (''.join(l))

if __name__ == '__main__':
    solution = Solution()
    resultado: str = solution.longest_common_prefix(["ab", "a"])
    esperado: str = "a"
    print(f"Resultado: {resultado}")
    print(f"esperado: {esperado}")
        