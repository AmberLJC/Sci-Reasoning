# Prior Work Analysis Report

## Target Paper
**Title:** 96I0XnrjkQ
**Conference:** Unknown 
**Authors:** Unknown

---

## Key Prior Works (7 papers)

---

## Synthesis

The paper’s core contribution—casting clustering as coalition formation in hedonic games with explicit friendship and enmity graphs and designing efficient local-deviation algorithms—sits at the confluence of two lines of work. From the hedonic-games literature, Banerjee–Konishi–Sönmez (2001) and Bogomolnaia–Jackson (2002) provide the foundational framework and deviation-based stability concepts (individual/Nash stability) that the paper adapts into its notions of local stability and local popularity for partitions. Subsequent work on algorithmic and representational aspects of hedonic games, especially Aziz–Brandt–Seedig (2014) on fractional hedonic games, shows how preferences can be encoded via weighted social ties and how stability/complexity trade-offs arise—directly motivating the paper’s compact, graph-based preference model and its complexity analysis.
On the clustering side, Bansal–Blum–Chawla (2004) established correlation clustering, which formalizes the friend/enemy (agree/disagree) view central to this paper’s mapping from similarity/dissimilarity to preferences, and legitimizes local-search style procedures. Raghavan–Albert–Kumara (2007) further influenced the algorithmic design through single-node label updates, a blueprint for efficient, scalable local improvement driven by neighborhood relations. Bridging these domains, Igarashi–Elkind (2016) demonstrated that graph-restricted hedonic games offer compact preference representations with tractable algorithms in certain cases, while Traag–Bruggeman (2009) validated the importance of signed networks for community detection. Collectively, these works directly inform the paper’s modeling choices (signed friendship/enemy graphs), stability notions (single-agent deviations), algorithmic mechanisms (local updates), and empirical focus (clustering and community detection).

---
*Generated: 2026-01-07T00:21:32.226898*
