import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS112025_030302_20(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 11 20 25 2.1.3 (4)' # 건설기준문서
    ref_date = '2020-12-03'  # 고시일
    doc_date = '2024-02-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '되메우기 및 뒤채움'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    되메우기 및 뒤채움
    3. 시공
    3.3 시공기준
    3.3.2 되메우기, 흙쌓기 및 땅고르기
    (20)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.2 되메우기, 흙쌓기 및 땅고르기
    (20) 측벽 되메우기는 토류벽과 구조물 외벽이 85 ㎝ 이하의 협소한 장소에서는 다짐작업이 불완전하므로 모래 또는 석분으로 채운 후 물다짐으로 침하가 발생치 않도록 하여야 한다.

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 측벽 되메우기];
    B["KCS 11 20 25 3.3.2 (20)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 25 3.3.2 (20)"])

    subgraph Variable_def
    VarIn1[/입력변수: 토류벽/];
    VarIn2[/입력변수: 구조물 외벽/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{토류벽 < 85 cm \n 외벽 < 85 cm}

    C --> |True|E[모래 또는 석분으로 채운 후 물다짐으로 침하가 발생치 않도록 하여야 한다.]
		E --> F([측벽 되메우기])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def side_wall_backfilling(fIEarWal, fIExtWal) -> RuleUnitResult:
        """측벽 되메우기

        Args:
            fIEarWal (float): 토류벽
            fIExtWal (float): 구조물 외벽

        Returns:
            sOSidBac (string): 측벽 되메우기
        """
        assert isinstance(fIEarWal, float)
        assert isinstance(fIExtWal, float)        

        if (fIEarWal <= 85) and  (fIEarWal <= 85):
            sOSidBac = "다짐작업이 불완전하므로 모래 또는 석분으로 채운 후 물다짐으로 침하가 발생치 않도록 하여야 한다."
            return RuleUnitResult(
                    result_variables = {
                        "sOSidBac": sOSidBac,
                    }
                )
        else:
            assert 1 != 1