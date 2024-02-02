import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020608_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.6.8 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '받침판 변형'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.8 지지판(backing plate) 설계
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
    A[받침판의 변형];
    B["KDS 24 90 11 4.2.6.8 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지지판의 전체 변형/];
		VarIn2[/입력변수: 응력/];
		VarIn3[/입력변수: 탄성한계/];

		VarIn1 & VarIn2 & VarIn3


		end

		Python_Class ~~~ Variable_def;
		Variable_def--->K


		K["<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;w_{1}&plus;\bigtriangleup&space;w_{2}\leq&space;h(0.45-2\sqrt{h/L})'>--------------------------------------------------------"];
		K --->M
		M(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Total_Deformation_Of_The_Support_Plate(fIDeltaw1Deltaw2,fIh,fIL) -> bool:
        """받침판 변형

        Args:
            fIDeltaw1Deltaw2 (float): 지지판의 전체 변형
            fIh (float): 높이
            fIL (float): 지지판길이

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.6.8 지지판(backing plate) 설계 (2)의 통과 여부
        """

        if fIDeltaw1Deltaw2 <= fIh*(0.4-2*(fIh/fIL)**0.5):
           return 'Pass'
        else:
           return 'Fail'


# 

