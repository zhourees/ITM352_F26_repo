# Try to append to a tuple. It won't work
# Name: Reesa Zhou
# Date: September 15, 2026

surveyRespondents = (1012, 1035, 1021, 1053);
surveyRespondents.append(1011);

surveyRespondents = surveyRespondents + (1011,)
print("Updated survey respondents:", surveyRespondents);
