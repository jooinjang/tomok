import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04100102_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.10.1.2 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계기준풍속'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 풍하중
    4.10.1 풍속
    4.10.1.2 설계기준풍속
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
        A[일반 중소지간 교량의 설계기준풍속];
        B["KDS 24 12 21 4.10.1.2 (1)"];
        A ~~~ B
        end
      subgraph Variable_def
    VarOut[/출력변수 : 설계기준풍속/];
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?V_{D}=40m/s'>"];
    E(["설계기준풍속"]);
    Variable_def--->D--->E
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_wind_speed(fOVD) -> float:
        """설계기준풍속

        Args:
            fOVD (float): 설계기준풍속

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.10.1.2 설계기준풍속 (1) 의 값
        """

        return(fOVD)


# 

