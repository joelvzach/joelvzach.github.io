---
layout: essay
title: "Under the coding hood: Angelhack Bangalore Hackathon 2018"
subtitle: "Angelhack is a famous organization that organizes hackathons around the globe, touching several cities worldwide, few of which lie in India…"
date: 2018-07-12 00:00:00 
categories: [events]
read_time: 6
medium_link: ""
---

---
### Under the coding hood: Angelhack Bangalore Hackathon 2018
Angelhack is a famous organization that organizes hackathons around the globe, touching several cities worldwide, few of which lie in India and Bangalore being one of the most competitive ones. I had booked the ticket to participate in this hackathon a long time ago, and so when the D-day was nearing, took a train and reached the metropolitan city. Bindya my college friend was already staying in Bangalore so it was just the two of us going for our very first hackathon, and it sure felt a bit scary.
#### The introduction
My cousin got me to the venue, CoWorks Space by 9 AM. It took some time finding our way through the huge complex and on the way met a fellow participant, Gaurav. He works at a company in Bangalore and came for the hackathon to spend the weekend building a product along with his two friends, Yeti and Puneet. We got to know one another better, and they were alright about letting the beginners, Bindya and I, join their team.
Surprisingly enough, we found our college Seniors at the hackathon as well, around 20 or so students from MEC. It was quite a pleasant feeling finding familiar faces, and it was fun watching them being all energetic and all.
MECians unite at Angelhack Bangalore Hackathon 2018Around 10 AM or so, the session began with the Angelhack Ambassador revealing to us that the theme of this years hackathon was _Seamless Technology_, and they were looking forward to hacks that involved such concepts. The hackathon had IBM as its global sponsor, while there were 3 API sponsors (Hypertrack, Agora.io, Hurrify). Code for a Cause, the none profit wing of Angelhack, was looking for hacks that solved social issues such as natural disasters and financial crisis. We were surprised to see over 90 participants and excellent ambiance that the hackathon had. At 11:30, the hackathon was officially launched.
#### Day 1
We decided to brainstorm the sub-topics that Code For A Cause had, and finally settled for the following idea that Puneet suggested: A local blockchain that is established in disaster-affected regions and the network is open to public donations which are air-drop/equally distributed amongst everyone in need. The digital financial support would provide the required support to survive the disaster.
So we decided to split up: Puneet and Yeti were working on generating the coins and the ledger for the blockchain, while Gaurav was working on the Website UI. Bindya and I did little research and explored the API’s offered by Agora.io and hypertrack.
In a few hours, they got the blockchain up and running. Around 10 PM, the organizers provided a session on how to pitch our idea to the panel and other relevant tips. Bindya left the venue by 8 PM and agreed to join back the next day in the morning.
The next challenge was deciding how to figure out the geographical locations of the users and pulling out the coordinates that fall within a specific zone. This is done using Geo-fencing, and we spent the night trying to find a way to do this. Initially, we tried to figure out a way to use Hypertrack API for geo-fencing, but it was not evident how to implement it. So we started looking for alternatives.
Puneet figured out that Batchgeo is a good alternative where one can paste excel table with latitude-longitude details, and the application generates the same on a world map. So this was the new plan:
- Make a database in a spreadsheet (classifying into zones)
- Paste the cells on Batchgeo
- Generate coordinates on world map
- download the KML file
- Convert KML to XML and use XQL to perform queries to find out the list of coordinates that fall within a disaster struck zone
- Use these coordinates to establish a blockchain
- Create an interface to accept donations via airdrops onto the network, and use the digital cash to meet immediate needs.
An image of the points that feel within a zone according to our databaseWe came to this conclusion after the entire night through. But when we hit road blocks, we would go to the recreational area and play fooseball (a net total of over 5 hours of that game XD), and have coffee from the automatic coffee maker at the cafeteria. Food kept rolling very often.
Yeti taking on the other two and winning in streaks of success!As the night grew darker, many started sleeping on whatever they could find. But being my first hackathon, I decided to stay awake through out the entire process to see how it felt.
**Day 2**
Everyone was semi-awake, just a second away from closing their eyes. The wise men who chose to sleep were now looking to see what others were upto, while the teams who stayed awake got to watch their project have an organic growth. It was around 5 AM while playing fooseball that I met [Vishal Arya](https://medium.com/u/b89580bb789e) and got to know him better. We shared quite a number of similarities, from exploring options to opinion about college life. You can read about his first experience being at a hackathon over [here](https://medium.com/@myfantasticj/how-i-attended-the-first-hackathon-of-my-life-ac0d80d0792d) .
After breakfast, it was a marathon for our team to keep up the pace after the long night of enjoyment. We decided to add more features to our application, such as a radio broadcast to talk about your problem to those in your locality (using Agora.io real time communication API’s) and a voice assistant to answer to your local needs and guide you in the disaster struck region.
Bindya and I made a video explaining what the product was from a template.
#### Judgement
Hackathon concluded by 1:30 and then we had to wait to pitch our idea to the panel. When the time finally came for presenting it, Puneet explained the idea very well, and answered questions from the panel. We were not able to explain everything due to poor internet connection. But despite that, the panel seemed interested in the solution based on “Proof Of Location” protocol that Gaurav, Yeti and Puneet developed.
#### Results
6 teams were shortlisted, but unfortunately we were not part of it. These were the distinctive ideas:
- An Application that converts sign language to text using machine learning ([Talking fingers](https://github.com/yuvi17/talking_fingers) by [Yuvraj Jaiswal](https://medium.com/u/946918119364))
- An Application that automates drone surveillance in buildings to find survivors of a disaster in real time — capable of expanding to user phones to help people support the drones.
- An Application that detects if a student is paying attention in class or not by analyzing the facial expressions
- An Application that detects texts from books and determines the source book it belonged to
- An Application that directly searches the internet for the errors we get while compiling our program, thus saving time
- An application that makes extensive use of Geo-fences.
It was interesting to see how much these participants were able to build from scratch.
#### Overall
To be honest, my lack of technical knowledge made me less of an asset towards the project, but Puneet, Yeti and Gaurav were kind and helpful to us and kept helping us find ways to contribute. I learned a lot of new points about blockchains and application development. It was a learning experience and I would recommend anyone to apply. If a beginner like me could make it through, so can you!
I plan to participate in more hackathons in the future, hopefully with more experience to make myself more valuable to the team.
