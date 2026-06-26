# MonteCar-Ball 🏀🎲

A Monte Carlo simulation that predicts an NBA team's season record by simulating thousands of seasons based on real player stats.

Built by Ahmed Mahmoud and Jason Noel as a fun side project to learn Python, APIs, and probability along the way.

---

## The Idea

Give it a roster of NBA players and it'll simulate that team's full 82-game season against the rest of the league thousands of times. The average win/loss record across all those simulations becomes the team's projected season outcome.

Player performance is pulled from real NBA stats via the [`nba_api`](https://github.com/swar/nba_api) package, and each simulated game is influenced by scoring averages and plus/minus impact.

---

## Status

🚧 **TO BE UPDATED** — actively in development.

- [ ] Data layer (pulling + caching player stats)
- [ ] Player / Team data structures
- [ ] Single game simulation
- [ ] Full season simulation
- [ ] Monte Carlo loop (thousands of seasons)
- [ ] Model validation against real historical results
- [ ] CLI for user-input rosters
- [ ] Stretch: full 30-team league + real schedule

---

## How It Works

**TO BE UPDATED** — short writeup once the model is locked in. Rough sketch for now:

1. Pull player season averages (points, plus/minus, etc.) from the NBA stats API
2. Build team objects from a list of players
3. Simulate a single game: each team's score is drawn from a distribution around their average, adjusted by net plus/minus
4. Repeat for 82 games to simulate one season
5. Repeat *that* thousands of times — average the results

---

## Project Structure

```
TO BE UPDATED — will fill in as folders get used
```

---

## Setup

```bash
# clone the repo
git clone https://github.com/your-username/MonteCar-Ball.git
cd MonteCar-Ball

# create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

---

## Usage

**TO BE UPDATED** — once `cli/main.py` is functional, add example commands here.

```bash
python cli/main.py
```

---

## Sample Output (target format)

This is the kind of output we're aiming to produce — not live yet:

```
Average Wins: 64.2
Average Losses: 17.8
Average PPG: 102.5
Average Point Differential: +8.4

Sample Seasons:
75-7
60-22
55-27

Highest Scorer: [Player]
Highest +/-: [Player]
Most Minutes: [Player]
```

---

## Notes / Open Questions

A running scratchpad for design decisions we're still figuring out. Update as we go.

- How much should plus/minus weight into score adjustment? (currently a placeholder value)
- Real schedule vs. simplified round-robin?
- How do we validate the model is actually realistic?

---

## Credits

- Stats via [`nba_api`](https://github.com/swar/nba_api)
- Built by [Jason] & [Friend]
