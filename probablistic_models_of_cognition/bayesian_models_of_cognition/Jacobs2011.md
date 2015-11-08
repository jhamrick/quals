Jacobs, R. A., & Kruschke, J. K. (2011). Bayesian learning theory applied to human cognition. Wiley Interdisciplinary Reviews: Cognitive Science, 2(1), 8–21. http://doi.org/10.1002/wcs.80

# Summary

Jacobs & Kruschke make an argument for using Bayesian models of cognition. They give a precise definition of what they mean for Bayesian models to be optimal, saying that given the structure of the prior and likelihood, Bayesian models are the optimal in the sense that you cannot do better. However, they also explicitly say that this is, of course *given that these structures are correct*. You can posit a variety of reasonable options for the structures in the model. They argue that this is a good thing, though, because it makes the assumptions explicit, which subsequently makes it more straightforward to evaluate those assumptions.

They give three examples of what can happen when comparing a Bayesian model to human behavior:

1. The model and human behavior match. This gives evidence that people are integrating information in a statistically optimal fashion, and provides support for the represenations used by the Bayesian model.
2. The model outperforms people. This suggests that people are not incorporating all sources of information, or are limited by computational constraints. These possibilities can be investigated by creating a new Bayesian model with these constraints.
3. People outperform the model. This suggests that people are taking into account more information or assumptions than the model. Again, this possibility can be investigated by creating a new model that accounts for more information.

Jacobs & Kruschke give examples of three ways in which Bayesian models can be used:

1. Inference: using data from some variables to update beliefs about other variables. Integrating data (e.g. multisensory percepts) in a statistically optimal fashion.
2. Parameter learning: similar to inference. They don't explicitly define what they take as being the difference between inference and parameter learning, but I think the difference for them is that inference is more about beliefs about causes, while parameter learning is more about learning the specific distributions of variables (e.g., inference --> did a or b cause c?, parameter learning --> what are the weights of a and b?). They do talk about the difference between *discriminative* and *generative* models, though:
    * discriminative: learning the conditional probability distribution p(outcome | cues)
    * generative: learning the joint probability distribution p(outcome, cues), from which you can compute p(outcome | cues) as well as p(cues | outcome)
3. Structure learning: not just learning about the variables in a model, but learning *which model* is the correct one.

They also briefly discuss how prior knowledge can be very influential, and how important it is to get right, and how you can determine what people's priors are.

They also talk about active learning, which is the process of actively selecting what data to observe. They argue that this process is not something that can be captured easily by other types of models.

# Methods

n/a

# Algorithm

n/a

# Takeaways

I like the characterization of what, exactly, it means for a Bayesian model to be "optimal", and what this implies for cognitive science. Importantly, they talk about the optimality of a Bayesian model as being a way to gauge what people are doing: are the suboptimal (implying processing limitations)? Or are they better than optimal (implying that the model is missing something?) Or are they close to the model (implying the model's assumptions may be close to what people actually do?)
