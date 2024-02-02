import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_04181002_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.10.2 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '감소계수'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.10.2 갑판실과의 충돌
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
        A[감소계수];
        B["KDS 24 12 21 4.18.10.2 (2)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 감소계수/];
    VarIn1[/입력변수 : 선박의 적재중량 톤수/];
    end
    Python_Class~~~Variable_def
    D{"선박이 100,000DWT 이상인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?R_{DH}=0.1'>"];
    F["<img src='https://latex.codecogs.com/svg.image?R_{DH}=0.2-(DWT/10,000)\times&space;0.10'>----------------------"];
    G(["감소계수"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
        """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def reduction_factor(fORdh,fIDWT) -> float:
        """감소계수

        Args:
            fORdh (float): 감소계수
            fIDWT (float): 선박의 적재중량톤수

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.10.2 갑판실과의 충돌 (2) 의 값
        """

        if fIDWT >= 100000:
          fORdh = 0.1

        else:
          fORdh = 0.2-(fIDWT/10000)*0.1

        return(fORdh)


# 

