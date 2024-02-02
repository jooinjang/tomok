import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_040302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.3.2 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '피로하중조합에 의해 유발된 응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.3 피로한계상태
    4.3.2 철근
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
    A["피로하중조합에 의해 유발된 응력"];
    B["KDS 24 14 21 4.3.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 피로하중조합에 의해 유발된 응력/];
		VarIn2[/입력변수: 피로하중조합에 의한 최소 활하중 응력/];
		VarOut1[/출력변수: 피로하중조합에 의해 유발된 응력/];
		VarOut1~~~VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def--->C--->F
		C["<img src='https://latex.codecogs.com/svg.image?&space;f_{fat}=166-0.33f_{min}'>---------------------------------"]
		C~~~~|KDS 24 12 11 Table 4.1-1|C

		F(["피로하중조합에 의해 유발된 응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Stresses_induced_by_fatigue_load_combinations(fOffat,fIfmin) -> float:
        """피로하중조합에 의해 유발된 응력

        Args:
             fOffat (float): 피로하중조합에 의해 유발된 응력
             fIfmin (float): 피로하중조합에 의한 최소 활하중 응력

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.3.2 철근 (1)의 값
        """

        fOffat = 166-0.33*fIfmin
        return fOffat


# 

