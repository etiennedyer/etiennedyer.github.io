As a child, I did not pay attention in class. I talked to the kids around me, had trouble focusing on and finishing assignments. As is quite common, I was diagnosed with predominantely inattentive ADHD. My mother was emphatic about my not taking any medication for it, and so I made it through elementary and high school by the very force of my wits (albeit with pretty mediocre grades).I started university taking humanities courses, and eventually switched to math, which was demanding as I’d flunked my last year of high school math. I was doing ok, but still felt like it was taking me about 4x the time it should to do my homework, so I asked my family doctor for ADHD medication. He gave me 20mg / day of Vyvanse, which I eventually reduced to 10mg.

It worked great! I felt I had more energy, had an easier time focusing, was more productive and generally in a better mood. I didn’t take them every day, cause they made me feel kind of wired, so I usually took them on days where I had lots to do. But then, whenver I felt good or driven or focused I would think to myself “Did I take my meds?” and if I did, I’d feel like whatever happiness or drive or focus I’d felt was not “me.” I also realized that while it did seem like I got more stuff done while on my meds, I predominately took them when I had stuff to do — of course I got more stuff done. So I decided I would harness the power of statistics

I bought some empty pill capsules and filled 15 of them with 10mg vyvanse, and 15 with a similar amount powdered sugar. I then wrote a program which randomly assigned the 15 placebo days and 15 medication days over a month. I made a little 30-day advent calendar, and got my dad to run the program and fill each day with the appropriate pill.[^1] The program used a seed for repeatability, and my dad took a screenshot of the output for redundancy. I gave each day a score out of 5, and guessed whether I got a placebo or medication.

Here are the data, R code, and results.

```
library(dplyr)
library(ggplot2)

trial <- read.csv("data/vyvanse/trial.csv", header = FALSE)
generated <- read.csv("data/vyvanse/generated.csv", header = FALSE)
df <- cbind(trial, generated)

colnames(df) <- c("mood", "guess", "day", "generated")

# Count how many guesses were correct
sum(df$guess == df$generated)

# Separate the mood scores based on the placebo condition
med_day <- df$mood[df$generated == 1]
placebo_day <- df$mood[df$generated == 0]

# Perform a paired t-test
t_test_result <- t.test(med_day, placebo_day, alternative = "greater", paired = TRUE)

# Print the t-test result
print(t_test_result)

boxplot(mood ~ generated, data = df)
```

“mood” is the daily score out of 5, “guess” is my guess regarding what pill I took (0 for placebo, 1 for medication), “day” indicates which of the 30 days this is, and “generated” is the actual value for the pill I took (same values as “guess”)

Firstly, what was shocking to me was I had no ability to tell what days I got a placebo, despite feeling like I definitely could — I had 15 correct guesses, and 15 incorrect ones. A couple days out I’m realizing my guess relied on a specific physical sensation that also happens when I drink coffee, so it makes sense I was getting this wrong, but it was initially very surprising.

My mean mood on days I took a placebo is 3.58/5 and on medicated days is 4/5. However, a one-way, paired t-test gives a p-value of 0.1321 which is, as the kids say, not statistically significant.

I’d like to eventually run the experiment again for longer in order to have something statistically significant, but for now I feel like I got my answer.

[^1]: (So not technically a double-blind, but I’d wager he forgot the schedule pretty quickly.)
[^2]

