import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '현장타설 거더 교량의 하부 플랜지 두께'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.2 거더 교량
    4.7.2.3 현장타설 거더 교량
    (2)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["현장타설 거더 교량"];
    B["KDS 24 14 21 4.7.2.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:거더의 하부플랜지 두께/];
		VarIn2[/입력변수:철근콘크리트 거더 사이 순간격/];
		VarIn3[/입력변수:프리스트레스트 거더 사이 순간격/];

		VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def
		Variable_def--->D & E

		D["거더의 하부플랜지 두께>140mm"]
		E["거더의 하부플랜지 두께≥철근콘크리트 거더 사이 순간격x1/16 or 프리스트레스트 거더 사이 순간격x1/30 "]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Lower_flange_thickness_of_girder(fIlofltg, fIfinsgrc, fIingprg) ->bool:
        """현장타설 거더 교량의 하부 플랜지 두께
        Args:
             fIlofltg (float): 거더의 하부플랜지 두께
             fIfinsgrc (float): 철근콘크리트 거더 사이 순간격
             fIingprg (float): 프리스트레스트 거더 사이 순간격
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.2.3 (2) 설계기준에 따른 현장타설 거더 교량의 하부 플랜지 두께 적합여부
        """
        if fIlofltg > 140:
          if fIlofltg >= fIfinsgrc/16 or fIlofltg >= fIingprg/30:
            return "Pass"
          else:
            return "Fail"
        else:
          return "Fail"


# 

