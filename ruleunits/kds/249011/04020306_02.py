import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020306_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.6 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '받침'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.6 설계원리
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
    A[최대설계변형률];
    B["KDS 24 90 11 4.2.3.6 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 압축설계하중에 의한 설계변형률/];
		VarIn2[/입력변수: 설계이동변위에 의한 설계전단변형률/];
		VarIn3[/입력변수: 설계각회전에 의한 설계변형률/];
		VarIn4[/입력변수: 하중종류에 따른 계수/];
		VarOut1[/출력변수: 최대설계변형률/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ Variable_def;
		Variable_def-->E
		E{"차량 활하중에 의해 계산되는 경우"}
		E--Yes--->F
		E--NO--->G
		F & G--->H--->I

    F["<img src='https://latex.codecogs.com/svg.image?K_{L}=1.5'>--------------------------------------------------------"];
		G["<img src='https://latex.codecogs.com/svg.image?K_{L}=1.0'>--------------------------------------------------------"];
		H["<img src='https://latex.codecogs.com/svg.image?\varepsilon_{t,d}=K_{L}(\varepsilon&space;_{c,d}&plus;\varepsilon&space;_{q,d}&plus;\varepsilon&space;_{\alpha,d})'>--------------------------------------------------------"];
		I(["최대설계변형률"])

  """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_Design_Strain(fOmaxdst, fIepsiloncd, fIepsilonqd, fIepsilonalphad, fIKL,fIuserdefined) -> float:
        """받침

        Args:
            fOmaxdst (float): 최대설계변형률
            fIepsiloncd (float): 압축설계하중에 의한 설계변형률
            fIepsilonqd (float): 설계이동변위에 의한 설계전단변형률
            fIepsilonalphad (float): 설계각회전에 의한 설계변형률
            fIKL (float): 하중종류에 따른 계수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.6 설계원리 (2)의 값
        """
        #일반적인 경우 > fIuserdefined == 1
        #차량 활하중에 의해 계산되는 경우 > fIuserdefined == 2

        if fIuserdefined == 1:
          fIKL = 1.0
        if fIuserdefined == 1:
          fIKL = 1.5
        fOmaxdst = fIKL*(fIepsiloncd+fIepsilonqd+fIepsilonalphad)
        return fOmaxdst


# 

