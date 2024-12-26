import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04020701_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.7.1 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '세장한 자유돌출판의 저감계수'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    4.2.7.1 세장한 자유돌출판
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[세장한 자유돌출판] ;
		B["KDS 14 31 10 4.2.7.1(3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 세장한 자유돌출판의 저감계수/]
    VarIn1[/입력변수: ㄱ형강의 가장 긴 다리의 폭/]
    VarIn2[/입력변수: 부재의 두께/]
    VarIn3[/입력변수: 강재의 항복강도/]
    VarIn4[/입력변수: 강재의 탄성계수/]
		end

		Python_Class ~~~C1(["KDS 14 31 10 4.2.7.1 (3)"]) -->Variable_def

	  C["<img src='https://latex.codecogs.com/svg.image?Q_{s}'>------"] ;
    D["<img src='https://latex.codecogs.com/svg.image?b/t\leq&space;0.45\sqrt{E/F_{y}}'>---------------------------------------------"] ;
    E["<img src='https://latex.codecogs.com/svg.image?0.45\sqrt{E/F_{y}}<b/t\leq&space;0.91\sqrt{E/F_{y}}'>----------------------------------------------------------------------------"] ;
     F["<img src='https://latex.codecogs.com/svg.image?b/t>0.91\sqrt{E/F_{y}}'>----------------------------------"] ;
     G(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.0'>-----------------------"]) ;
    H(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=1.34-0.76\left(\frac{b}{t}\right)\sqrt{\frac{F_{y}}{E}}'>---------------------------------------------------------------"]) ;
    I(["<img src='https://latex.codecogs.com/svg.image?Q_{s}=\frac{0.53E}{F_{y}\left(\frac{b}{t}\right)^{2}'>-----------------------------------"]) ;

	  Variable_def-->C-->D & E & F
    D-->G
    E-->H
    F-->I
    """

    @rule_method
    def Reduction_factor_of_slender_free_projection_plate(fOQs,fIb,fIt,fIFy,fIE)-> RuleUnitResult:
        """세장한 자유돌출판의 저감계수

        Args:
            fOQs (float): 세장한 자유돌출판의 저감계수
            fIb (float): 자유돌출판의 폭
            fIt (float): 부재의 두께
            fIFy (float): 강재의 항복강도
            fIE (float): 강재의 탄성계수


        Returns:
            fOQs (float): 강구조부재설계기준(하중저항계수설계법) 4.2.7.1 세장한 자유돌출판  (3)의 값
        """

        assert isinstance(fOQs, float)
        assert isinstance(fIb, float)
        assert fIb > 0
        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fIFy, float)
        assert fIFy > 0
        assert isinstance(fIE, float)
        assert fIE > 0

        if fIb/fIt <= 0.45*(fIE/fIFy)**0.5:
          fOQs = 1.0

        elif fIb/fIt > 0.45*(fIE/fIFy)**0.5 and fIb/fIt <= 0.91*(fIE/fIFy)**0.5:
          fOQs = 1.34 - 0.76*(fIb/fIt)*(fIFy/fIE)**0.5

        else:
          fOQs = 0.53*fIE/(fIFy*(fIb/fIt)**2)

        return RuleUnitResult(
          result_variables = {
            "fOQs": fOQs,
            }
        )