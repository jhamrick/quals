Griffiths, T. L., & Tenenbaum, J. B. (2006). Optimal predictions in everyday cognition. Psychological Science, 17(9), 767–773. http://doi.org/10.1111/j.1467-9280.2006.01780.x

# Summary

Griffiths and Tenenbaum basically ask, how sensitive are people to the statistics of their environment? They test this by asking people to give estimates of total durations $t_\mathrm{total}$ given an observation at some time $t$. They find that people's estimates of $t_\mathrm{total}$ are consistent with empirical priors and uniform likelihoods.

# Methods

They asked people to make judgments on:

* Life spans
* Movie runtimes
* Movie grosses
* Poems
* Representatives
* Pharoahs
* Cakes
* Waiting times

# Algorithm

The algorithm is pretty simple, just computing $p(t_\mathrm{total}|t)\propto p(t|t_\mathrm{total})p(t_\mathrm{total})$ and assuming a uniform likelihood. The priors are determined empirically and have the following approximate forms:

* Gaussian (life spans, movie runtimes)
* Power law (movie grosses, poems)
* Erlang (representatives, pharoahs)
* Irregular (cakes)
* ??? (waiting times)

They also empirically fit a parameterized distribution for pharaohs and waiting times. In the case of the pharaohs, people systematically overestimated (but the empirical prior recovered from people was consistent with their posterior judgments). In the case of waiting times, there is not a consensus what distribution they take, though according to people their responses seemed to fit an power law distribution.

# Takeaways

People are sensitive to the structure and statistics of their environments. In cases where they have less experience/exposure (e.g. in the case of the pharaohs), people aren't necessarily optimal with respect to the true empirical distribution, but may instead rely on other knowledge (e.g. modern monarchs) and attempt to generalize.
