import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04010504_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.1.5.4 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수평 및 수직하중'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.5 모듈러형 신축이음(Modular Expansion Joint)
    4.1.5.4 윤하중 분배
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
    A[윤하중 분배];
    B["KDS 24 90 11 4.1.5.4 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 수평 및 수직하중/];

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D-->E

		C{"단부보 설계시"}
		D["KDS 24 90 11 4.1.5.3"]
		E["윤하중분배=수평 및 수직하중X50%"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Horizontal_And_Gravity_Load (fIhoravl) -> float:
        """수평 및 수직하중
        Args:
            fIhoravl (float): 수평 및 수직하중

        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.1.5.4 윤하중 분배 (1)의 값
        """

        return fIhoravl*0.5


# 

