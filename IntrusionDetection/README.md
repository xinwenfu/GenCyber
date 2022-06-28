WEBVTT

1
00:00:05.069 --> 00:00:07.799
Xinwen Fu: Okay, so any questions, no questions.

2
00:00:09.900 --> 00:00:10.710
kylesavoie: I think i'm all set.

3
00:00:11.219 --> 00:00:12.030
Xinwen Fu: Okay yeah.

4
00:00:12.059 --> 00:00:23.790
Xinwen Fu: So let's go over the slides quickly i'm going to speak quickly, but I found if I speak quickly, I often pronounce something wrong but it's Okay, and so.

5
00:00:24.600 --> 00:00:43.950
Xinwen Fu: This is the part of our story today, you know plan right, and so we are going to talk about the intrusion detection system in the morning and we will talk about the firewall so we actually can see here, this is the big picture of.

6
00:00:45.060 --> 00:00:53.940
Xinwen Fu: This lecture right we first talked about intrusion detection away, we needed so when we talk about the firewall you know if I always not enough, then we'll talk about why we intrusion detection.

7
00:00:54.960 --> 00:01:04.380
Xinwen Fu: So, once we understand the idea of intrusion detection and we'll talk about where we're going to deploy intrusion detection systems we deployed.

8
00:01:04.800 --> 00:01:18.150
Xinwen Fu: The intrusion detection system at a host at a computer, we can also deployed at you know, a network at all just within the networks and we can also deploy this Angelica.

9
00:01:19.140 --> 00:01:31.080
Xinwen Fu: You know at the temperature water right, and so this is the idea of our positioning intrusion detection systems, now we will talk about the intrusion prevention, the pre program basically is.

10
00:01:32.070 --> 00:01:44.070
Xinwen Fu: Using firewalls to block everything and then we'll talk about some real world examples and as an example of intrusion detection, we are going to use this.

11
00:01:45.090 --> 00:01:58.500
Xinwen Fu: Protocol and an either or the wire shark wire shark is not a real intrusion detection software, but you can use wire shark to perform intrusion detection so, then we are going to introduce the handle.

12
00:01:59.250 --> 00:02:11.100
Xinwen Fu: Okay, and so this is the big picture of cyberspace when we try to defend our campus network right, so you can see just the Internet on the lab the rest of.

13
00:02:11.610 --> 00:02:24.900
Xinwen Fu: All the components belong to our entity, for example, our you mess low, and so we discussed that you know, we need a the external firewall we the internal firewall.

14
00:02:25.530 --> 00:02:33.090
Xinwen Fu: To protect actually this D amp D right, but really it's a thorough firewall which defines.

15
00:02:33.630 --> 00:02:43.380
Xinwen Fu: The dmz, and so we host a like a web server email server other servers within the m&e so that even you know the servers within the dmca.

16
00:02:43.800 --> 00:03:00.840
Xinwen Fu: A compromised, you know the cannot actually I mean the bad guys cannot get into our campers competitors directly right that's why we have the internal firewall blocking direct access to other campers computers.

17
00:03:02.070 --> 00:03:05.250
Xinwen Fu: Then, as we already learned, you know.

18
00:03:06.390 --> 00:03:07.170
Xinwen Fu: firewalls.

19
00:03:08.430 --> 00:03:25.290
Xinwen Fu: cannot defeat other attacks by because sometimes there are no attacks firewalls are normally used to to block know no attacks so that's why we need the intrusion detection system.

20
00:03:26.130 --> 00:03:40.230
Xinwen Fu: So well approach that intrusion detection system uses is to check if the network traffic is normal or not, but you can see here the intrusion detection system collects.

21
00:03:40.830 --> 00:03:49.800
Xinwen Fu: Network traffic from every computer maybe maybe not every computer but promote many computers on campus and see if it's normal, for example.

22
00:03:50.490 --> 00:04:09.210
Xinwen Fu: let's say, for example, suddenly, you see a huge amount of traffic compared to yesterday now, you may think oh man what's happening here right maybe he's a denial of service attack somebody sending a huge amount of attack a traffic traffic traffic try to actually congested our.

23
00:04:10.230 --> 00:04:12.630
Xinwen Fu: Network right so that's why we.

24
00:04:13.740 --> 00:04:17.700
Xinwen Fu: Have a doing intrusion detection and so.

25
00:04:19.020 --> 00:04:30.810
Xinwen Fu: We already actually learned what is interesting discussion, but the here's a formal definition so intrusion detection is a process of identifying and responding to malicious activity.

26
00:04:31.410 --> 00:04:42.660
Xinwen Fu: target enter computing and the networking resources right, and so this is called intrusion detection and intrusion detection system.

27
00:04:43.830 --> 00:04:57.510
Xinwen Fu: can be software can be hardware, but anyway, if it's harder it's do like a software inside the hardware right and that they perform the intrusion detection Okay, and so this is a normally.

28
00:04:59.820 --> 00:05:00.450
Xinwen Fu: How.

29
00:05:02.790 --> 00:05:23.910
Xinwen Fu: an intrusion detection system is a programmed always works okay this This shows the components of an intrusion detection system so here don't over there is a cardiac computers, this may be a lot of competitors and then we're going to collect network, a package from this red.

30
00:05:25.230 --> 00:05:29.910
Xinwen Fu: You know, protect computers, we want to see you for this computer is performing no money or not.

31
00:05:31.290 --> 00:05:41.220
Xinwen Fu: So, once you actually capture other trapping, then you can see, here we have someone costing called a sensor here, this is just kind of like a software here and analyzing.

32
00:05:42.210 --> 00:05:50.340
Xinwen Fu: The collected, a network of packets and see you put there's anything wrong by, for example, if there are no attacks and if.

33
00:05:50.760 --> 00:05:58.260
Xinwen Fu: that's too much traffic something like that, and you can see here, basically, this decision making mechanical refers to.

34
00:05:58.740 --> 00:06:16.620
Xinwen Fu: be the basis right configuration and here you can see it as knowledge something, for example, know attacks and so basically this a sensor here checks the traffic and referring to no knowledge.

35
00:06:17.880 --> 00:06:29.280
Xinwen Fu: To find evil, there are a text or not, so if there are attacks some intrusion detection system may actually.

36
00:06:30.270 --> 00:06:39.660
Xinwen Fu: Try to respond, for example, one response is that we just actually turn off of our network right so that's the one kind of.

37
00:06:40.080 --> 00:06:54.540
Xinwen Fu: action here we just block everything and that we need to actually check what's wrong with those particular computers right, so this is normally how you know at the is it works and that there are components.

38
00:06:57.240 --> 00:07:01.350
Xinwen Fu: Okay, so now let's look at where we put her intrusion detection systems.

39
00:07:03.180 --> 00:07:06.990
Xinwen Fu: So first let's look at her actually something called a.

40
00:07:08.100 --> 00:07:14.760
Xinwen Fu: host based intrusion detection system, but before we do that so let's look at the Internet right we already did this before we already.

41
00:07:15.120 --> 00:07:27.870
Xinwen Fu: introduced, what is the Internet that you can see here, but you know middle here the block task over there are like a routers and you know that we have so those waters responsible.

42
00:07:29.220 --> 00:07:48.750
Xinwen Fu: You know, relating your messages from end to end right from your to your friend or your mom or your dad or something like that, and you can see, also you know, there are many other routers which are managed by the ISP like a comcast and we're reading and those companies, so those waters.

43
00:07:49.800 --> 00:08:09.000
Xinwen Fu: They work together and the actually forward our messages to the destination you, am very efficient away by them in the middle, is the you know kind of transportation network that at the end now, we have our.

44
00:08:10.050 --> 00:08:16.620
Xinwen Fu: local networks here that you can see, here we have different a customer networks One example is that you must know.

45
00:08:17.610 --> 00:08:39.030
Xinwen Fu: Network so within us know you know we have so many computers so basically maybe we actually use the department as a unit so each department has their own network that we can add as a local area network but it's really kind of a relative or concept here and.

46
00:08:40.140 --> 00:08:44.760
Xinwen Fu: So that's how actually Internet it's a structured.

47
00:08:45.870 --> 00:08:59.460
Xinwen Fu: So let's first look at what is the host based intrusion detection system, so a host based intrusion detection system basically will stay on a single computer.

48
00:09:00.240 --> 00:09:08.010
Xinwen Fu: And sometimes it could be a software, but most of time we use a software programs as intrusion detection systems, for example.

49
00:09:08.610 --> 00:09:22.320
Xinwen Fu: i'm not sure if you heard of a snort snort is a software package which can be used for intrusion detection Okay, so you can use still stored on your computer and snort will collect.

50
00:09:22.800 --> 00:09:31.530
Xinwen Fu: Your network traffic and the snot will analyze your package right entering your computer and a demon your computer and.

51
00:09:32.310 --> 00:09:44.100
Xinwen Fu: And there's Nord can also actually check the log files on your computer and a snort can also actually, for example, check out the processes and assistance running on your computer okay.

52
00:09:44.730 --> 00:09:58.800
Xinwen Fu: And so, this is the what host the intrusion detection system will do most of the time, but you can see here and sometimes you know as a science are the ones is right, we actually refined.

53
00:09:59.490 --> 00:10:11.970
Xinwen Fu: host based intrusion detection system and so that they can do more, we can protect better our computers so One example is called a protocol department, what does this mean it means.

54
00:10:12.510 --> 00:10:32.910
Xinwen Fu: When you run your browser by we are you are using the http protocol to brass website, and so the Protocol implemented means we want to make sure the particle is a properly followed not entry changed by the attack okay.

55
00:10:34.560 --> 00:10:49.620
Xinwen Fu: So where is the host based intrusion detection system is on your local computer here, so you can see here on each local computer right, and so we have the host based intrusion detection okay system.

56
00:10:51.420 --> 00:11:09.120
Xinwen Fu: Then the next type of intrusion detection system, he said, the network of basically intrusion detection, that you can see here right, so we call this network intrusion detection basically means you know this system will collect traffic from all.

57
00:11:10.350 --> 00:11:24.330
Xinwen Fu: The computers on the network so basically whatever goes through the cable right and this network of based intrusion detection system will dump it and that will analyze.

58
00:11:24.870 --> 00:11:37.350
Xinwen Fu: The network packet Okay, so I saw I said something wrong you've done, I mean an idea is done actually collector you know, since, from your host, but it will just.

59
00:11:37.980 --> 00:11:47.070
Xinwen Fu: interceptor all network packets passing along the network cable Okay, and so you can see here and.

60
00:11:47.940 --> 00:11:56.610
Xinwen Fu: send it to an ad by host So you can see here the host of me stand actually done it as their local files, of course, host to that that's okay and.

61
00:11:57.510 --> 00:12:10.800
Xinwen Fu: and also here, you can see pratensis and the system running around and that there were holes it before you want to actually do that Okay, and so this is about the whole network based intrusion detection system and.

62
00:12:12.930 --> 00:12:13.860
Xinwen Fu: So you can see here.

63
00:12:15.780 --> 00:12:23.430
Xinwen Fu: So the reason the other ones is intrusion detection for the network intrusion detection, so you know.

64
00:12:25.980 --> 00:12:40.680
Xinwen Fu: At the beginning intrusion detection system is designed for owning detection, but as time goes we find, sometimes with how to respond to the attack.

65
00:12:41.220 --> 00:12:50.040
Xinwen Fu: that's why you can see here and for recent other one is of our network based intrusion detection system.

66
00:12:50.730 --> 00:13:05.190
Xinwen Fu: We may have a key rules means that we're going to do something not just passively analyzing the network of packets we're going to actually shut down the trouble making connections okay.

67
00:13:06.720 --> 00:13:13.380
Xinwen Fu: So where is a networker based intrusion detection system on the Internet okay.

68
00:13:14.520 --> 00:13:17.010
Xinwen Fu: So basically, you can see.

69
00:13:18.150 --> 00:13:31.620
Xinwen Fu: The soldier is a intrusion detection system Okay, the network based intrusion detection system, it will just collect the traffic from the cable Okay, and so.

70
00:13:32.370 --> 00:13:41.310
Xinwen Fu: You can see here, you know the network intrusion detection says, I mean the network based intrusion detection seasons is kind of a.

71
00:13:42.090 --> 00:14:06.930
Xinwen Fu: More than the host based intrusion detection system, as we saw here right and so basically the metal rock up is interested in system will click traffic, maybe locks from anywhere within this a local area networks Okay, and so it's more than host based intrusion detection system.

72
00:14:09.000 --> 00:14:27.660
Xinwen Fu: OK now let's look at the sort of hip hop intrusion detection system called a perimeter based intrusion detection system, and so the perimeter based intrusion detection system, you can see, normally isn't little kids aren't around Rod, so you know.

73
00:14:29.400 --> 00:14:36.210
Xinwen Fu: Our campers has something called an agile water, we should stays on the edge of the network.

74
00:14:36.990 --> 00:14:48.180
Xinwen Fu: Which means all your network, a package will go through the router because the router is responsible for forwarding your packets, to the destination right.

75
00:14:48.480 --> 00:15:00.570
Xinwen Fu: You must have done the House so many edge routers maybe I think, maybe two or three at Reuters, which are responsible for data poppers Okay, and you can see that's very important and.

76
00:15:01.590 --> 00:15:13.200
Xinwen Fu: We need to protect those edge routers right and because you know those edge routers can see all incoming traffic from Internet Maybe those traffic.

77
00:15:14.190 --> 00:15:30.090
Xinwen Fu: Are from the bad guys, so if we put an intrusion detection system and the added water that we will form our first line of Defense right so basically that's.

78
00:15:30.660 --> 00:15:37.560
Xinwen Fu: Why, we need it, this kind of a perimeter based intrusion detection system, and this kind of system will analyze.

79
00:15:38.160 --> 00:15:50.400
Xinwen Fu: Can you can see network of packets passes through the gateway router right and anything you know, on the router and the blocks process is fence on the on the router or gateway okay and.

80
00:15:52.830 --> 00:16:06.510
Xinwen Fu: Recent advances in intrusion prevention in terms of our perimeter based intrusion detection system so here the key idea here is, you know because of the routers these the attack.

81
00:16:08.580 --> 00:16:15.000
Xinwen Fu: realtor is the first to see the attacks right, and so the router should be able to block.

82
00:16:15.450 --> 00:16:25.830
Xinwen Fu: The attacks once it happens, of course, we had to think about how to do that, but we call that as, as do ladies in blocking me see if there's any attack the water will block it.

83
00:16:26.670 --> 00:16:32.490
Xinwen Fu: You know right and, at the earliest time and, but the deal is a blocking is not easy okay and.

84
00:16:33.330 --> 00:16:48.150
Xinwen Fu: And so it because you know, think about that right, and there are so much traffic going through the router and can you actually inspect all the network packets, one by one, and that is impossible so it's very challenging to do this okay.

85
00:16:50.040 --> 00:16:50.820
Xinwen Fu: So here is a.

86
00:16:51.870 --> 00:17:03.300
Xinwen Fu: The perimeter basic intrusion detection system on the Internet it's just at the edge of our camera network that's normally where we put her the piano yes okay.

87
00:17:04.560 --> 00:17:15.420
Xinwen Fu: Okay, so we talked about you know intrusion detection, another important concept is intrusion prevention and So what does the intrusion prevention, you know.

88
00:17:15.930 --> 00:17:24.990
Xinwen Fu: intruder provision means that we want to actually prevented the attack right and so that's why we call this intrusion prevention, and so one challenge.

89
00:17:26.040 --> 00:17:26.670
Xinwen Fu: For.

90
00:17:27.900 --> 00:17:33.720
Xinwen Fu: intrusion detection is a, how can we perform the real time intrusion detection and.

91
00:17:36.120 --> 00:17:38.040
Xinwen Fu: For today's Internet.

92
00:17:39.510 --> 00:17:56.190
Xinwen Fu: It accrues huge amount of that traffic at a tremendous speed and a really it's a very challenge to actually detect attacks among so much traffic in real time.

93
00:17:57.210 --> 00:18:10.770
Xinwen Fu: You know either you use software right, you know software is where so sometimes you know and sulfur Muslim time cannot do real time intrusion detection that's why you know many people now.

94
00:18:12.060 --> 00:18:32.040
Xinwen Fu: turn to hardware for intrusion detection, so we use a hardware to implement the intrusion detection algorithms so that we can actually perform real time intrusion detection, but it's still a very big challenge, think about the speed and the amount of traffic right and.

95
00:18:33.450 --> 00:18:35.640
Xinwen Fu: So that's a bigger problem okay.

96
00:18:40.050 --> 00:18:40.530
Xinwen Fu: So.

97
00:18:43.140 --> 00:18:43.650
Xinwen Fu: You know.

98
00:18:47.640 --> 00:18:48.570
Xinwen Fu: So basically.

99
00:18:51.630 --> 00:19:04.080
Xinwen Fu: We know we want to do intrusion detection and we also wanted to intrusion prevention, but how can you do intrusion detection intrusion prevention.

100
00:19:05.100 --> 00:19:06.030
Xinwen Fu: effectively.

101
00:19:07.980 --> 00:19:15.660
Xinwen Fu: So I just showed you guys the merits plot and a motivator payload.

102
00:19:16.950 --> 00:19:40.380
Xinwen Fu: If you already analyzed such Member that you know it's features that you can actually try to detect such kind of features in a network packets see if it is a witness plot payload on that right Paul know attacks it's a either to block it right, but.

103
00:19:42.000 --> 00:19:42.960
Xinwen Fu: In reality.

104
00:19:44.040 --> 00:19:54.030
Xinwen Fu: There is so much traffic over there, even for example you create the features for an attack, how can you guarantee in such features.

105
00:19:55.350 --> 00:19:59.580
Xinwen Fu: Are not existing in other kind of a normal traffic.

106
00:20:01.830 --> 00:20:14.580
Xinwen Fu: By and then maybe another application will create a similar traffic your features will not actually be effective Okay, so that could be a problem.

107
00:20:15.600 --> 00:20:20.400
Xinwen Fu: And a lot of challenges to intrusion prevention is let's see you know you know.

108
00:20:21.480 --> 00:20:31.560
Xinwen Fu: There are so many possibilities, you may block the wrong traffic right that's called a false positive was it's not real attack, but you think a test.

109
00:20:32.070 --> 00:20:40.980
Xinwen Fu: But you think fine I just don't want anybody to attack me i'm going to block everything that is suspicious event is not a real attack.

110
00:20:41.790 --> 00:20:55.530
Xinwen Fu: Okay, however that's good for your home if you want to do that, but can and as to do that know if as P blocks too much traffic you'll be fearless because you know.

111
00:20:56.430 --> 00:21:08.820
Xinwen Fu: me tell you, most of the intrusion detection systems, how huge number of pasta potatoes, you will be queries and if we did the plot that because you know.

112
00:21:09.480 --> 00:21:19.350
Xinwen Fu: You will be blocked a lot okay so that's a problem, a lot of ways to live in fear right for intrusion detection and prevention, you know, there are so much traffic how much time.

113
00:21:19.860 --> 00:21:29.070
Xinwen Fu: Does it take to analyze the traffic and the funded attack so that's another problem here right and but anyway, people have been thinking about this, you know.

114
00:21:29.580 --> 00:21:39.330
Xinwen Fu: How do we do intrusion prevention and detection together essentially it's an ongoing challenge, but we are the ones in other ways to how not opportunities.

115
00:21:41.010 --> 00:21:51.060
Xinwen Fu: So Okay, I want to show you so why we do the intrusion detection intrusion prevention here so basically, you can see here right you use the firewalls and you can do prevention.

116
00:21:51.630 --> 00:21:59.760
Xinwen Fu: Because you know, sometimes you can prevent it for sure, and also, you can do detection here, you can see, all my my goodness today in the traffic.

117
00:22:00.480 --> 00:22:14.850
Xinwen Fu: From another computer prominent it is huge I don't like that, as think it's bad I think most of time it is like maybe the top three so attack traffic so i'm going to block it, so in this way because you've you found the huge amount of.

118
00:22:16.980 --> 00:22:28.050
Xinwen Fu: Traffic from not a computer is not normal you can detect okay that may be an attack you can block it right, however, you know if it's a zero day attacks music new attack.

119
00:22:28.920 --> 00:22:49.890
Xinwen Fu: Then the attacker will compromise your computer, so this will happen, and you know that's why, when you still study intrusion prevention and detection and see if you can find the attacks and, but this is a reality in the word okay.

120
00:22:51.240 --> 00:22:56.790
Xinwen Fu: So we have this cast the intrusion detection intrusion prevention let's look at some real world examples.

121
00:22:58.410 --> 00:23:18.030
Xinwen Fu: So let's look at a warm called a sequel some warm So what is the warm a warm is one kind of software this software can discover valuable computers on the Internet, then this warm and these are Member can send it itself to those compromised computers and.

122
00:23:19.110 --> 00:23:23.370
Xinwen Fu: The mobile we work again on those compromised computers and again.

123
00:23:24.570 --> 00:23:29.370
Xinwen Fu: The malware on those computers will try to find other bonobo computers on the Internet and.

124
00:23:30.060 --> 00:23:38.310
Xinwen Fu: In fact, the other computers, but you can see here, using this approach, the warmth can propagate itself too many, many computers.

125
00:23:38.760 --> 00:23:49.050
Xinwen Fu: Right from one company to another company from an eloquent two or more computers so that's why we call this as a warm because this mirror can propagate itself.

126
00:23:49.980 --> 00:24:12.210
Xinwen Fu: autonomously OK, and a sequel stem war was the fastest Internet warm my hour right you history, so this is what happened on July 24 2002 Microsoft allows Okay, we found a problem now, you can see here as upon everybody was not a so kind of a sanity or two attacks.

127
00:24:14.160 --> 00:24:14.580
Xinwen Fu: In.

128
00:24:15.600 --> 00:24:25.710
Xinwen Fu: tucson and to the bother ability was last, then you put on the three these sequels now worm was the end dished.

129
00:24:27.000 --> 00:24:27.810
Xinwen Fu: And then.

130
00:24:28.890 --> 00:24:39.210
Xinwen Fu: At this point, okay somebody's Father oh there's a sequel stem warmer just remember running on the Internet, but as our pond you know.

131
00:24:40.470 --> 00:24:41.700
Xinwen Fu: It already a fighter.

132
00:24:42.720 --> 00:24:52.860
Xinwen Fu: 90% of vulnerable hosts within 10 minutes Okay, and then you can see how fast, this can be right, because you know as we mentioned that the warmer can propagate itself.

133
00:24:53.760 --> 00:25:06.720
Xinwen Fu: And so what is the woman the woman is a mirror so basically the warm will send out the malware payload the code and in a single UDP packet so the whole.

134
00:25:07.860 --> 00:25:18.180
Xinwen Fu: Mailer can be put into a packet and the whole payload right the whole hour is only 376 Bytes.

135
00:25:19.350 --> 00:25:19.800
Xinwen Fu: So.

136
00:25:22.050 --> 00:25:28.530
Xinwen Fu: This payload right this packet it send it to a server that's the word athlete runs.

137
00:25:30.180 --> 00:25:39.000
Xinwen Fu: At a port 1434 okay so basically if you didn't upgrade your server.

138
00:25:40.290 --> 00:25:41.490
Xinwen Fu: Does sequel server.

139
00:25:43.470 --> 00:25:51.960
Xinwen Fu: Then, if you're somewhere less at the port 14 so therefore this.

140
00:25:52.980 --> 00:26:02.940
Xinwen Fu: malware will compromise your computer, as we did in our laps, then you can imagine, once you know these a.

141
00:26:04.740 --> 00:26:10.500
Xinwen Fu: Mailer right this worm compromise your computer what will happen right, the whole thing is compromised okay.

142
00:26:11.220 --> 00:26:25.590
Xinwen Fu: And so that's what happened now how can you this is shows actually how fast it affects everything here, you can see right and before and after the warmer you can see so many computers that were compromised okay and.

143
00:26:27.540 --> 00:26:37.980
Xinwen Fu: So how can you stop a decent warmer, how can you stop this attack of costs, you mean the first patch your server so that you know, there is no such programming.

144
00:26:39.180 --> 00:26:49.320
Xinwen Fu: era in your cell phone animal because there's no standard era may mean when the malware tries to attack data port, it will not work.

145
00:26:49.890 --> 00:27:03.570
Xinwen Fu: Now you can also use a firewall have to block the traffic at targeting port 1434 right and so that's what you do, you can also use vpn so anybody has to use vpn to access.

146
00:27:04.290 --> 00:27:13.200
Xinwen Fu: The server right in this way, you know basically you health firewall blocking everything you have to use vpn to access its port number and the Member will now work.

147
00:27:13.710 --> 00:27:29.310
Xinwen Fu: Okay, and so, because you know these are 14 so therefore it's a one on YouTube I mean, why not protocol, you know so basically you can actually do the intrusion detection premium, but at that point, nobody cared about cybersecurity that's why you know.

148
00:27:30.900 --> 00:27:39.180
Xinwen Fu: There was a huge impact when the my work was released on the Internet Okay, and here we see the Ladies in.

149
00:27:39.990 --> 00:27:52.110
Xinwen Fu: A queue ids ids is only way of a blog and this warm do digital means Okay, once you find the attack and you know it's attack Okay, and once you see the packet you'll notice attack you know.

150
00:27:52.680 --> 00:28:02.010
Xinwen Fu: That require some knowledge, the accurate means you block the warm basically it means you drop the packets.

151
00:28:03.030 --> 00:28:04.110
Xinwen Fu: Center by this.

152
00:28:05.340 --> 00:28:17.430
Xinwen Fu: malware right and so basically that's how you do it, but it's ready to change up the new attack or the new way where you don't know right you don't know all the knowledge right, and how can do that that's a big challenge.

153
00:28:19.350 --> 00:28:34.560
Xinwen Fu: So I want to talk about were shocked so we're shock is a software program and the worst shock can actually capture network packets into your computer and then going out offer your computer and to show all the packets.

154
00:28:36.180 --> 00:28:40.890
Xinwen Fu: offer the network, a panga clapping Okay, and so.

155
00:28:42.060 --> 00:28:58.980
Xinwen Fu: So let's look at the interface here, and so this is the interface when you click were shocked right, you can find it on windows vm now, this is the interface, you will see, and then you will see different network cards and so these were shocked come.

156
00:29:00.720 --> 00:29:03.180
Xinwen Fu: dump all network traffic.

157
00:29:05.430 --> 00:29:10.290
Xinwen Fu: going out of these Internet card or.

158
00:29:12.600 --> 00:29:23.820
Xinwen Fu: coming into this ethernet card Okay, and so, when you click it basically workshop, we will begin to capture other network package that you can see here, this is a.

159
00:29:24.630 --> 00:29:31.650
Xinwen Fu: All the commands recommended menus and here is a display filter because there's so much traffic here, and you don't want to see all the.

160
00:29:31.950 --> 00:29:42.030
Xinwen Fu: packages, sometimes, then you can actually set up a filter, for example, in this case, we see an IP data source, this means Okay, and the within the packet right.

161
00:29:43.140 --> 00:29:55.620
Xinwen Fu: The source IP is a ten.zero.to.us 2016, and here the destination IP is a ten.zero.to dot the 30 here, so you would only want to see.

162
00:29:56.070 --> 00:30:07.950
Xinwen Fu: Okay, a packet which has such a kind of a source IP and destination IP or the other way Okay, so that this is what this a display filter means you just want to.

163
00:30:08.460 --> 00:30:17.610
Xinwen Fu: show the traffic by with such kind of a pack the header you don't want to see other traffic and then in this panel, here we show the details of.

164
00:30:19.350 --> 00:30:28.590
Xinwen Fu: select the regular header so when you click a packager in this panel here, and it will show you actually hear the headers of.

165
00:30:29.970 --> 00:30:41.220
Xinwen Fu: Those packets, the data single package, and you can see here there's a lot of a header here, so you had to actually come to college to learn everything here Okay, but if you actually.

166
00:30:42.510 --> 00:31:03.060
Xinwen Fu: click the packet it also show you the banner content, so what is the real data with them the packet of course right the headers here a part of the banner content but, as you know, most of the data here how minions.

167
00:31:04.170 --> 00:31:10.890
Xinwen Fu: Some of the data here refer to the headers each header has their own meanings each.

168
00:31:12.060 --> 00:31:24.600
Xinwen Fu: Maybe data here is a field within the headers so what we're shot does best is it will show you what each data means.

169
00:31:25.560 --> 00:31:45.960
Xinwen Fu: In this panel here, so this will actually help you understand that the particles, so when you actually learn Internet protocols and these Sabra will help you allowed telling you what each field means and what is that the name okay this how this is a very useful software.

170
00:31:47.040 --> 00:31:47.340
Xinwen Fu: Okay.

171
00:31:48.870 --> 00:31:55.110
Xinwen Fu: So, so, so this is basically what is going on here and and then we have a hands on lab right so for the hands on lab.

172
00:31:56.160 --> 00:32:00.750
Xinwen Fu: What I wanted, what do we want to do here is, you know we are going to deploy.

173
00:32:02.160 --> 00:32:10.620
Xinwen Fu: We are going to deploy the knock attack that can sell windows vm and I want you guys to use wire shark to capture the attack of traffic.

174
00:32:11.130 --> 00:32:24.000
Xinwen Fu: And so the question for you is a can you actually find the attacker packets, send a prom carry wham to windows so that's basically what am I going to do with intrusion detection here.

175
00:32:25.200 --> 00:32:27.750
Xinwen Fu: I think that that's all, let me actually stop recording.

