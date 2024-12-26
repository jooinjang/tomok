import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS112025_020103_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = False # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 11 20 25 2.1.3 (4)' # 건설기준문서
    ref_date = '2020-12-03'  # 고시일
    doc_date = '2024-02-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '되메우기 및 뒤채움'    # 건설기준명

    description = """
    되메우기 및 뒤채움
    2. 자재
    2.1 재료
    2.1.3 뒤채움 재료
    (4)
    """
    content = """
    #### 2.1.3 뒤채움 재료
    (4) 도로공사 시 뒤채움 시공에 사용하는 재료는 표 2.1-1의 품질기준을 만족하여야 한다.

표 2.1-1 뒤채움 재료의 품질기준

\begin{table}[]
\begin{tabular}{|llll|}
\hline
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 선택층재료}}                                                                                                                                   & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 양질의 토사}}                                                  & \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                                \\ \cline{2-3}
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 구분}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}피토고1)\\ (3.5m 미만)\end{tabular}}}                                                                               & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}피토고\\ (3.5m 이상)\end{tabular}}} & \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 비고}}            \\ \hline
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 최대치수 (mm)}}            & \multicolumn{1}{l|}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} }}                                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100 이하}}                                                  & {\color[HTML]{333333} }                                                        \\ \cline{1-1} \cline{3-4}
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 5 mm 통과량}}             & \multicolumn{1}{l|}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} }}                                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{A30200} \textbf{25 $\sim$100}}}                                   & {\color[HTML]{333333} }                                                        \\ \cline{1-1} \cline{3-4}
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 0.08 mm 통과량}}          & \multicolumn{1}{l|}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} }}                                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 15 이하}}                                                   & {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}노상기준:\\ 25\% 이하\end{tabular}} \\ \cline{1-1} \cline{3-4}
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 소성지수 (PI)}}            & \multicolumn{1}{l|}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} }}                                                                                                                     & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10 이하}}                                                   & {\color[HTML]{333333} }                                                        \\ \cline{1-1} \cline{3-4}
\rowcolor[HTML]{FFFFFF}
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 수정 CBR (\%)}}          & \multicolumn{1}{l|}{\multirow{-5}{*}{\cellcolor[HTML]{RGBA(139, 209, 111, 0.71)}{\color[HTML]{044406} \begin{tabular}[c]{@{}l@{}}KCS 44 50 05\\ 표 2.2-1, 표 2.2-2\\  \\ 보조기층재료와 동등한\\ 기준의 재료\end{tabular}}}} & \multicolumn{1}{l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10 이상}}                                                   & {\color[HTML]{333333} }                                                        \\ \hline
\rowcolor[HTML]{FFFFFF}
\multicolumn{4}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 주 1) 피토고 산정기준은 암거 중심선의 상단에서 길어깨부를 제외한 도로 유효폭원까지의 최소높이를 말한다.}}                                                                                                                                                                                                                                                                                                                                                                                       \\ \hline
\end{tabular}
\end{table}


    """
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 도로공사 뒤채움 재료의 품질기준];
    B["KCS 11 20 25 2.1.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 25 2.1.3 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 피토고/];
    VarIn2[/입력변수: 최대치수/];
		VarIn3[/입력변수: 5 mm 통과량/];
		VarIn4[/입력변수: 0.08 mm 통과량/];
		VarIn5[/입력변수: 소성지수/];
		VarIn6[/입력변수: 수정 CBR/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{피토고 < 3.5 m}

    C --> |True|D{"구분"}
    D --> |최대\n치수|F["KCS 44 50 05\n 표 2.2-1, 표 2.2-2\n보조기층재료와 동등한기준의 재료"]
		D --> |5 mm \n통과량|F
		D --> |0.08mm \n통과량|F
		D --> |소성\n지수|F
		D --> |수정 CBR|F

    C --> |False|E{"구분"}
    E --> |최대\n치수|G["100 이하"]
		E --> |5 mm \n통과량|H["25~100"]
		E --> |0.08mm \n통과량|I["15 이하\n(노상기준: 25% 이하)"]
		E --> |소성\n지수|J[10 이하]
		E --> |수정 CBR|L[10 이상]

		F --> M([뒤채움 재료의 품질기준])
		E --> M
		G --> M
		H --> M
		I --> M
		J --> M
	  L --> M
    """

    @rule_method
    def quality_standards_for_backfill_material(fIHeiRoa, bIMaxSiz, bIPasAmo_1, bIPasAmo_2, bIPlaInd, bIModCBR) -> RuleUnitResult:
        """
        Args:
            fIHeiRoa (float): 피토고
            bIMaxSiz (bool): 최대치수
            bIPasAmo_1 (bool): 5 mm 통과량
            bIPasAmo_2 (bool): 0.08 mm 통과량
            bIPlaInd (bool): 소성지수
            bIModCBR (bool): 수정 CBR

        Returns:
            sOQuaBac (string): 뒤채움 재료의 품질기준
        """
        assert isinstance(fIHeiRoa, float)
        assert isinstance(bIMaxSiz, bool)
        assert isinstance(bIPasAmo_1, bool)
        assert isinstance(bIPasAmo_2, bool)
        assert isinstance(bIPlaInd, bool)
        assert isinstance(bIModCBR, bool)
        assert (bIMaxSiz + bIPasAmo_1 + bIPasAmo_2 + bIPlaInd + bIModCBR) == 1

        if fIHeiRoa < 3.5:
            if bIMaxSiz == True:
                sOQuaBac = "KCS 44 50 05 표 2.2-1, 표 2.2-2 보조기층재료와 동등한 기준의 재료"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIPasAmo_1 == True:
                sOQuaBac = "KCS 44 50 05 표 2.2-1, 표 2.2-2 보조기층재료와 동등한 기준의 재료"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIPasAmo_2 == True:
                sOQuaBac = "KCS 44 50 05 표 2.2-1, 표 2.2-2 보조기층재료와 동등한 기준의 재료"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIPlaInd == True:
                sOQuaBac = "KCS 44 50 05 표 2.2-1, 표 2.2-2 보조기층재료와 동등한 기준의 재료"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIModCBR == True:
                sOQuaBac = "KCS 44 50 05 표 2.2-1, 표 2.2-2 보조기층재료와 동등한 기준의 재료"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
        else:
            if bIMaxSiz == True:
                sOQuaBac = "100 이하"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIPasAmo_1 == True:
                sOQuaBac = "25 ~ 100"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIPasAmo_2 == True:
                sOQuaBac = "15 이하"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIPlaInd == True:
                sOQuaBac = "10 PI 이하"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )
            elif bIModCBR == True:
                sOQuaBac = "10 % 이상"
                return RuleUnitResult(
                    result_variables = {
                        "sOQuaBac": sOQuaBac,
                    }
                )