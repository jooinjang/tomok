import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_010303_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 1.3.3(2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-21'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '콘크리트 구조의 연성요구조건'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    1. 일반사항
    1.3 설계원칙
    1.3.3 연성
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
     A[연성 요구조건];
     B["KDS 24 10 11 1.3.3 (2)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 연결부의 저항/];
    VarIn2[/입력변수 : 최대 하중효과/];
    end
    Python_Class~~~Variable_def
    D{"콘크리트 구조인 경우"};
    E["연결부의 저항 &ge; 1.3 X인접구성요소의 비탄성 거동에 의해 발생하는 최대 하중효과"];
    F(["Pass or Fail"]);
    Variable_def--->D--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def resistance_of_connection(fIrescon,fILemax) -> bool:
        """콘크리트 구조의 연성요구조건

        Args:
            fIrescon(float): 연결부의 저항.
            fILemax (float): 최대 하중효과.

        Returns:
            bool: 교량 설계 일반사항(한계상태설계법) 1.3.3(2) 연성요구조건을 만족하는지 여부
        """

        if fIrescon>=1.3*fILemax:
            return 'Pass'
        else:
            return 'Fail'


