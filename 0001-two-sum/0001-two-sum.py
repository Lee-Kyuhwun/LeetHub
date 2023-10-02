from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 숫자와 그 인덱스를 저장할 빈 딕셔너리 생성
        num_map = {}
        
        # 리스트의 숫자들을 순회
        for index, num in enumerate(nums):
            # 현재 숫자와 목표 값의 차이 계산
            diff = target - num
            
            # 차이가 이미 딕셔너리에 있는지 확인
            if diff in num_map:
                return [num_map[diff], index]  # 두 숫자의 인덱스 반환
            
            # 현재 숫자와 그 인덱스를 딕셔너리에 추가
            num_map[num] = index
            
        # 쌍을 찾지 못한 경우 (문제에서는 항상 하나의 해결책이 있다고 가정)
        return []
