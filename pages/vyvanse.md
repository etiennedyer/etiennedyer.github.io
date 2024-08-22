# An n=1 trial on the effects of Vyvanse

As a child, I did not pay attention in class. I'd get up and walk around unprompted, distracted other kids, had trouble focusing on and finishing assignments... As is quite common, I was diagnosed with ADHD,  predominantely inattentive. My mother was emphatic about my not taking any medication for it, and so I made it through elementary and high school by the very force of my wits (albeit with pretty mediocre grades). I started university taking humanities courses, and eventually switched to math, which was demanding as I’d flunked my last year of high school math. I was doing ok, but still felt like it was taking me about 4x the time it should to do my homework, so I asked my family doctor for ADHD medication. He gave me 20mg / day of Vyvanse, which I eventually reduced to 10mg.

It worked great! I felt I had more energy, had an easier time focusing, was more productive and generally in a better mood. I didn’t take them every day, cause they made me feel kind of wired, so I usually took them on days where I had lots to do. But then whenever I felt good or driven or focused I would think to myself “Did I take my meds?” and if I did, I’d feel like whatever happiness or drive or focus I’d felt was not “me.” I also realized that while it did seem like I got more stuff done while on my meds, I usually took them when I had stuff to do — of course I got more stuff done. So I decided I would harness the power of statistics to get to the bottom of this.

I bought some empty gelatin pill capsules and filled 15 of them with 10mg vyvanse, and 15 with a similar amount powdered sugar. I then wrote a Python program which randomly assigned the 15 placebo days and 15 medication days over a month. I made a little 30-day advent calendar, and got my dad to run the program and fill each day with the appropriate pill. [^1] The program used a seed for repeatability, and my dad took a screenshot of the output for redundancy. I gave each day a score out of 5 for some blend of mood and drive and focus, and guessed whether I got a placebo or medication. My initial guess was that I'd see an improvement of ~ 20% on medicated days.

You can find the data, Python code for scheduling, and R code for data analysis [here](https://etiennedyer.github.io/assets/vyvanse/code.md).

So, what were the results? Firstly, I was shocked to discover that I had no ability to tell what days I got a placebo, despite feeling like I definitely could: I had 15 correct guesses and 15 incorrect ones, no better than a coin flip. A couple days out I’m realizing my guess relied on a specific physical sensation that also happens when I drink coffee, so it makes sense I was getting this wrong, but it was initially very surprising.

My mean mood on days I took a placebo is 3.58/5 and on medicated days is 4/5, so an improvement of ~ 11%, just over half what I guessed. However, a one-way, paired t-test [^2] gives a p-value of 0.1321 which is, as the kids say, not statistically significant.

<a>
  <img src="https://etiennedyer.github.io/assets/vyvanse/boxplot.png" height=300>
</a>

I’d like to eventually run the experiment again for longer in order to have something statistically significant, but for now I feel like I got my answer. That being said, I do think "yo-yo"ing between medicated days and unmedicated days made the latter less productive — I've been off the meds for a few days, and I feel like I'm not "waiting" for the extra energy. I've kept tracking my mood, so maybe I'll run the experiment again with 2 weeks on / 2 weeks off.

[^1]: So not technically a double-blind, but I’d wager he forgot the schedule pretty quickly.
[^2]: One-way since I was testing whether Vyvanse had a positive effect, not just any effect, and paired because both sets of measurements were from the same sample (me!)

