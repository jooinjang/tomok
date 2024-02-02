import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010202_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단철근이 없는 부재의 설계전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
    (4)
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
    A["설계전단강도"];
    B["KDS 24 14 21 4.1.2.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarIn1[/입력변수: 최소설계전단강도/];
		VarIn2[/입력변수: ηl/];
		VarIn3[/입력변수: 콘크리트의 재료계수/];
		VarIn4[/입력변수: k/];
		VarIn5[/입력변수: 주인장 철근비/];
		VarIn6[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn7[/입력변수: fn/];
		VarIn8[/입력변수: 단면의 복부폭/];
		VarIn9[/입력변수: 단면의 유효깊이/];
		VarIn10[/입력변수: 콘크리트 하위 0.05분위 기준인장강도/];
		VarIn11[/입력변수: 절대건조 밀도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8~~~~ VarIn10 & VarIn11

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D
		Variable_def--->F
		C["<img src='https://latex.codecogs.com/svg.image?\eta&space;_{1}=0.4&plus;0.6\gamma&space;_{g}/2200'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?V_{cd,min}=(0.35\eta&space;_{1}\phi&space;_{c}f_{ctk}&plus;0.15f_{n})b_{w}d'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?V_{cd}=[0.7\eta&space;_{1}\phi&space;_{c}\kappa(\rho&space;f_{ck})^{1/3}&plus;0.15f_{n}]b_{w}d'>---------------------------------"]

		D & F--->G
		G(["설계전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_shear_strength_without_shear_rebar(fOVcd,fIVcdmin,fIetal,fIphic,fIk,fIrho,fIfck,fIfn,fIbw,fId,fIfctk,fIgammag) -> float:
        """전단철근이 없는 부재의 설계전단강도

        Args:
             fOVcd (float): 설계전단강도
             fIVcdmin (float): 최소설계전단강도
             fIetal (float): 절대건조밀도에 따른 전단강도 보정계수
             fIphic (float): 콘크리트의 재료계수
             fIk (float): 유효깊이 변화에 따른 전단강도 보정계수
             fIrho (float): 주인장 철근비
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도
             fIfn (float): 축응력
             fIbw (float): 단면의 복부폭
             fId (float): 단면의 유효깊이
             fIfctk (float): 콘크리트 하위 0.05분위 기준인장강도
             fIgammag (float): 절대건조 밀도

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.2 전단보강철근이 없는 부재 (4)의 값
        """

        fIeta = 0.4 + 0.6*fIgammag/2200
        fIVcdmin = (0.35*fIetal*fIphic*fIfctk + 0.15*fIfn)*fIbw*fId
        fOVcd = max((0.7*fIetal*fIphic*fIk*(fIrho*fIfck)**(1/3) + 0.15*fIfn)*fIbw*fId, fIVcdmin)

        return fOVcd


# 

