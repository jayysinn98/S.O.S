##Characters
define player = Character("[name]")
define eye = Character("Eye", image = "eye.jpg")

##images
image black = im.Scale("black.jpg", 1920, 1080)
image nus = im.Scale("NUS.jpg",1920, 1080)
image pap = im.Scale("pap.jpg", 1920, 1080)
image concert = im.Scale("concert.jpg", 1920, 1080)
image cheat = im.Scale("cheat.jpg", 1920, 1080)
image sgsafe = im.Scale("sgsafe.jpg", 1920, 1080)
image jobMale =  im.Scale("malejob.jpg", 1920, 1080)
image jobFemale = im.Scale("femalejob.jpg", 1920, 1080)
image homo = im.Scale("homo.jpg", 1920, 1080)
image redsg = im.Scale("redsg.jpg", 1920, 1080)
image condo = im.Scale("condo.png", 1920, 1080)
image mbs = im.Scale("mbs.jpg", 1920, 1080)
image daughterMale = im.Scale("daddaughter.jpg", 1920, 1080)
image daughterFemale = im.Scale("momdaughter.jpg", 1920, 1080)
image ndp = im.Scale("ndp.jpg", 1920, 1080)
image unhappy = im.Scale("happy.jpg", 1920, 1080)
image prison = im.Scale("prison.jpg", 1920, 1080)
image gun = im.Scale("gun.jpg", 1920, 1080)

##score variables
define gender = "M"
define threatScore = 0
define moralScore = 50
define happyScore = 0

init python:
    def change(var, amt) :
        var += amt
        if var > 100 :
            var = 100
        elif var < 0 :
            var = 0
        return var


screen happiness:
    text "{color=#ff0000}Happiness : [happyScore]{/color}" xpos 0.05 ypos 0.05

# Add to string : og_string += "\Dumbo"
label start:
    scene black
    $ name = renpy.input("What is your name?")
    $ name = name.strip()

    "Hello [name]! Welcome to my Gaming Life Project : S.O.S!"
    centered "Before we start, just some questions for you to answer to get to know you a little better"
    centered "What is your gender?"
    menu :
        "Female":
            $ gender = "F"
        "Male" :
            $ gender = "M"

    centered "How happy are you with your life now?"
    menu :
        "Satisfied!" :
            $ happyScore += 75
        "Not the best, but I don't exactly hate it":
            $ happyScore += 25
        "Indifferent..." :
            $ happyScore += 50
        "Unhappy" :
            $ happyScore += 0
        "Very happy" :
            $ happyScore += 100
    centered "Thoughts on the Singapore government?"
    menu :
        "Could be better.." :
            $threatScore += 40
            $moralScore += 20
        "Excellent" :
            $threatScore += 10
            $moralScore += 50
        "Neutral" :
            $threatScore += 30
            $moralScore += 30
        "Get me out man" :
            $threatScore += 50
            $moralScore += 10
        "Good" :
            $threatScore += 20
            $moralScore += 40

    centered "Between you and me... any crimes committed before? (regardless of whether you were caught or not)"
    menu :
        "Yeah..." :
            $threatScore += 20
        "Honestly? No" :
            $threatScore += 0

label inSchool:
    show screen happiness
    scene nus
    "Alright [name]! Let's start the game proper!"
    "Here, you will be a student in the National University of Seenguhpour!"
    "Let's see where your choices take you!"
    "Try to avoid being unhappy for too long!"
    "You can check your score on the top left corner!"
    "Let's begin!"

    "As we all know, every university student picks 2 of the 3 S's"
    "Which of the 3 will you give up?"
    menu : ##chooseS
        "Sleep" :
            $moralScore = change(moralScore, 10)
            $happyScore =change(happyScore, 20)
        "Studies" :
            $moralScore = change(moralScore, -20)
            $happyScore = change(happyScore, 20)
        "{color=#ff0000}Social Life{/color}" :
            $moralScore = change(moralScore,10)
            $happyScore = change(happyScore, -20)
    centered "Interesting choice..."
    centered "So the semester goes by...and..."
    with fade

    scene concert
    centered "{color=#000000}Your favourite band is in town this weekend!{/color}"
    centered "{color=#000000}Unfortunately you have exams next week :/ {/color}"
    "Do you attend the concert?"
    menu : #concert to go anot
        "{color=#ff0000}YES!!!{/color}" :
            $moralScore = change(moralScore, -20)
            $happyScore =change(happyScore, 20)
        "Nah... exams take precedence" :
            $moralScore = change(moralScore, 10)
            $happyScore =change(happyScore, -20)
    with fade

    scene black
    centered "The week and concert day passes... and exams are fast approaching..."
    centered "There has been this module you and your friends have been struggling with, but luckily, the final is online!"
    centered "But the Professor has explicitly stated no discussion even though the exam is open book..."
    centered "Your friends ask if you would like to do the exam in the same room so as to facilitate discussion"
    scene cheat
    "What do you do?"
    menu: #friend cheating in exam
        "{color=#ff0000}Grades are be all end all. Let's cheat!{/color}" :
            $threatScore = change(threatScore, 20)
            $moralScore = change(moralScore, -20)
            $happyScore = change(happyScore, 10)
            "Phew, you and your friends managed to secure an A- !"
        "No cheating...reluctantly..." :
            $moralScore = change(moralScore, 10)
            $happyScore = change(happyScore, -10)
            "With your integrity intact, you duly obtain a B- for the module..."
        "Report your friends to the Professor" :
            $moralScore = change(moralScore, 20)
            $happyScore = change(happyScore, -10)
            "With a B+, you thoroughly outshone your (former) friends who got Fs!"
    with fade

    scene sgsafe
    centered "{color=#000000}With terrorism a major world issue today, the government has actively pushed for citizens to download the SafeSG app, to pinpoint citizens' locations in times of emergencies{/color}"
    centered "{color=#000000}Do you download the app?{/color}"
    menu : #download location app
        "Of course! Safety is my priority!" :
            $moralScore = change(moralScore, 20)
            "Now, with the app, you feel much safer leaving your home"
        "{color=#ff0000}Seems fishy... better not...{/color}" :
            $moralScore = change(moralScore, -10)
            "Thankfully, nothing happened subsequently to warrant the download"

    scene black
    centered "Having survived university... you now move onto adulthood! Congratulations!"

label adulthood :
    scene black
    centered "Ah...the working world...time to face reality..."
    centered "You and your close friend Jeff apply for the same dream job, hoping to work together..."
    #EVENT : JOB INTERVIEW
    if gender == "M":
        show jobMale
    elif gender == "F":
        show jobFemale
    if moralScore > 50 :
        call getJob from _call_getJob
    else :
        call noGetJob from _call_noGetJob
    with fade
    scene black
    centered "A couple of years go by, you are happily married, own a car, and relatively happy at your workplace"
    centered "Suddenly, terrible news strike : The country's Prime Minister has suffered a heart attack"
    centered "On the day people are allowed to pay their respects, your friends ask you over for a couple of rounds of Mahjong"
    centered "What do you do?"
    #CHOICE : MAHJONG OR VISIT
    menu :
        "{color=#ff0000}Mahjong, without a doubt! The PM ain't related to me anyway...{/color}" :
            $moralScore = change(moralScore, -20)
            $happyScore = change(happyScore, 10)
            $threatScore = change(threatScore, 20)
        "Definitely decline the game which can take place any other day" :
            $moralScore = change(moralScore, 20)
            $happyScore = change(happyScore, -10)
            $threatScore = change(threatScore, -10)
    "May he rest in peace..."
    if moralScore == 0 :
        jump gameOverMoral
    if happyScore == 0 :
        jump gameOverHappy
    with fade

    #EVENT : GET CAR
    scene redsg
    centered "{color=#000000}On one of your off days, you decide you want to explore a particular park that is far from home{/color}"
    centered "{color=#000000}However, your spouse is out with the car, and won't be back anytime soon{/color}"
    centered "{color=#000000}So you head over to your carpark, wanting to try RedSG : the country's car sharing platform!{/color}"
    if moralScore > 50 :
        call getCar from _call_getCar
    else :
        call noGetCar from _call_noGetCar
    with fade

    #CHOICE : LGBTQ SUPPORT
    scene homo
    centered "{color=#000000}Following news of yet more homophobia in the country, some students of NUS, your alma mater, have begun calling government authorities out{/color}"
    centered "{color=#000000}Others have called for stricter punishments for people who incite such hate{/color}"
    centered "{color=#000000}You come across one such post on Instagram...{/color}"
    centered "{color=#000000}What do you do?{/color}"
    menu:
        "Like the post to show my support, nothing more incase it becomes controversial for you" :
            $moralScore = change(moralScore, -10)
            $threatScore = change(threatScore, 10)
        "Ignore the post and continue scrolling" :
            $moralScore = change(moralScore, 20)
            $threatScore = change(threatScore, -10)
        "{color=#ff0000}Share the post on your stories, and search for other similar posts so that you can do the same{/color}":
            $moralScore = change(moralScore, -20)
            $threatScore = change(threatScore, 20)
    if threatScore > 80 :
        jump gameOverThreat
    if moralScore == 0 :
        jump gameOverMoral
    with fade


    #EVENT : HOUSING
    scene condo
    centered "{color=#000000}Over the years of working hard and saving, you finally can afford premium housing, an upgrade in terms of amenities and location on your current flat!{/color}"
    centered "{color=#000000}However, this is subject to a first come first serve basis, so the housing is not guaranteed, but no harm trying right?{/color}"
    centered "{color=#000000}So you submit your application early on for the current window, and duly await the news...{/color}"
    with fade
    centered "{color=#000000}2 weeks later, you see a letter from the Housing Committee...{/color}"
    if moralScore > 60 :
        call getCondo from _call_getCondo
    else :
        call noGetCondo from _call_noGetCondo
    with fade

    #CHOICE : CHARITY
    scene mbs
    centered "It's the end of the year, and your company has given you a free staycation at the popular Marinara Day Sends!"
    centered "To your horror, it clashes with your annual 'Charity Day' where you volunteer at a nearby community centre"
    centered "Ahhh which do you choose to do?"
    menu :
        "{color=#ff0000}Staycay all day every day!{/color}":
            $moralScore = change(moralScore, -20)
            $happyScore = change(happyScore, 20)
        "Still volunteer, but book your own staycay which doesn't clash with Charity Day" :
            $moralScore = change(moralScore, 10)
            $happyScore = change(happyScore, -10)
            centered "Unfortunately, Marinara Day Sends did not have anymore available rooms, forcing you to settle for an alternative..."
    if moralScore == 0 :
        jump gameOverMoral
    if happyScore == 0 :
        jump gameOverHappy
    with fade

    #EVENT : CHILD SCHOOLING
    if gender == "M":
        show daughterMale
    elif gender == "F":
        show daughterFemale
    centered "{color=#000000}Now that you are happily married with a daughter, you are getting ready to send your child to primary school!{/color}"
    centered "{color=#000000}Being the Asian parent that you are, you are determined to send your child to the best school : Ruffles Girls' Primary!{/color}"
    centered "{color=#000000}Having indicated the school as your top choice, you eagerly await the news, knowing this could potentially shape your daughter's entire future{/color}"
    centered "{color=#000000}Then, you receive a text from the Ministry of Education...{/color}"
    if moralscore > 50 :
        call getSchool from _call_getSchool
    else :
        call noGetSchool from _call_noGetSchool
    with fade

    #CHOICE : 50th ANNIV
    scene ndp
    centered "{color=#000000}Years go by and the country's 50th birthday is coming!{/color}"
    centered "Public places are open everywhere for people to get together to celebrate"
    centered "However, being ever so patriotic, you are torn between waiting, in boredom, for the evening celebrations and taking a half-day trip to Seenguhpour's neighbour, Murrleisher"
    menu :
        "Stay and chill at home then head out in the evening" :
            $moralScore = change(moralScore, 10)
        "{color=#ff0000}No time to waste, let's head out of the country!{/color}" :
            centered "To your surprise, there are many others just like you, resulting in a jam on both legs of the journey, causing you to miss the celebrations entirely..."
            centered "You had fun nonetheless!"
            $happyScore = change(happyScore, 10)
            $moralScore = change(moralScore, -20)
            $threatScore = change(threatScore, 20)
    if threatScore > 80 :
        jump gameOverThreat
    if moralScore == 0 :
        jump gameOverMoral
    if happyScore == 0 :
        jump gameOverHappy
    jump gameOverMoral

######## EVENTS LABELS #################
#EVENT : JOB
label getJob :
    centered "{color=#000000}The news comes in and you got the job!{/color}"
    centered "{color=#000000}You call Jeff to ask if he did as well.{/color}"
    centered "{color=#000000}To your dismay, he didn't. Then you recall that he wasn't the most well behaved back in school so maybe that played a part...{/color}"
    centered "{color=#000000}Nonetheless, you are employed! Congratulations!{/color}"
    return

label noGetJob :
    centered "{color=#000000}The news comes in and unfortunately you didn't get the job...{/color}"
    centered "{color=#000000}Jeff, on the other hand, got it, though there is no animosity between the 2 of you given your friendship{/color}"
    centered "{color=#000000}You begin to wonder what went wrong since the 2 of you had the exact same credentials...and the interview went well...{/color}"
    centered "{color=#000000}Be that as it may, you manage to find another job, which isn't so bad afterall!{/color}"
    $happyScore = change(happyScore, -10)
    return

##EVENT : CAR
label getCar :
    centered "{color=#000000}Though it is your first time trying the app out, everything works like a charm and you reach the park, all ready to explore mother nature!{/color}"
    return

label noGetCar :
    centered "{color=#000000}Upon opening the application, you run into regular bugs and problems. For some reason, the car refused to start{/color}"
    centered "{color=#000000}After trying for almost 10 minutes, you decide that you are no longer in the mood, and head back home, to much annoyance.{/color}"
    $happyScore = change(happyScore, -10)
    return

#EVENT : HOUSE
label getCondo :
    centered "{color=#000000}As it turns out, there were spaces available and you have found yourself a new home!{/color}"
    centered "{color=#000000}Time to pack your bags!{/color}"
    return

label noGetCondo :
    centered "{color=#000000}Somehow, there were no units available anywhere for you...{/color}"
    centered "{color=#000000}Back to your current house, till the next application window...{/color}"
    $happyScore = change(happyScore, -10)
    return

#EVENT : SCHOOL
label getSchool :
    centered "{color=#000000}Your child has been successfully registered for RUFFLES' GIRLS PRIMARY SCHOOL. Please report to school on 5TH JANUARY 8:00AM.{/color}"
    centered "{color=#000000}Knowing this, you take your family out for a celebration!{/color}"
    return

label noGetSchool :
    centered "{color=#000000}Your application for your child to enter RUFFLES' GIRLS PRIMARY SCHOOL has been rejected. Please select your next choice in the MOE website.{/color}"
    centered "{color=#000000}Crestfallen, you frantically search for ideal alternatives where your daughter can still have a good future...{/color}"
    $happyScore = change(happyScore, -20)
    return

############## GAME OVER LABELS #############################
label gameOverThreat:
    scene gun
    centered "{color=#ff0000}YOU HAVE BEEN DEEMED AS A MAJOR THREAT TO OUR DEMOCRACY. GOODBYE{/color}"
    return

label gameOverMoral:
    scene prison
    centered "{color=#ff0000}YOUR SCORE IS TOO LOW. NOT GOOD ENOUGH{/color}"
    centered "{color=#ff0000}YOU SHALL BE SENT FOR REFORMATION, INDEFINITELY{/color}"
    centered "{color=#ff0000}Not knowing what has hit you, you wonder if this has to do with your choices previously...{/color}"
    return

label gameOverHappy:
    scene unhappy
    centered "{color=#ff0000}Your happiness hit 0. You lost :({/color}"
    return
