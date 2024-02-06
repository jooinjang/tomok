import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_04_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 4.1' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계전단강도'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(1)
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
    A["전단설계"];
    B["KDS 24 17 10 부록.4.(1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:공칭전단강도/];
		VarIn2[/입력변수:강도감소계수/];



		VarOut1[/출력변수: 설계전단강도/];
		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def
		Variable_def--->D--->E--->F
		D["강도감소계수=1.0"]

		E["설계전단강도=공칭전단강도 x 강도감소계수"]

		F(["설계전단강도"])



    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_shear_strength(fOshstr,fInoshst,fIstrfac) -> float:
        """설계전단강도

        Args:
            fOshstr (float): 설계전단강도
            fInoshst (float): 공칭전단강도
            fIstrfac (float): 강도감소계수


        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (1)의 값
        """

        fOshstr = fInoshst * fIstrfac
        return fOshstr



# 
