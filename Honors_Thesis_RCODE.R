rm(list = ls())

library(ggplot2)
library(reshape2)
library(xlsx)
library(gridExtra)
getwd()

Data <- read.csv("/Users/Pablo/Desktop/R_out/CombinedData2.csv")
names(Data)


Data

sums <- colSums(Data[, c(-1,-24)])
Almostdata <- Data[, c(TRUE, sums > 0)]

newd <- Almostdata[,-19]

newd

newsums <- rowSums(newd[,-1])
newd$total <- with(newd, rowSums(newd[,-1]))

newd

newd2

newd2 <- t(newd)
groups <- newd[,1]

par(mar=c(5,12,4,1)+0.1, cex=0.8)
newnew <- newd[c(-18,-28,-29),]

newnew


OrdereredArray <- c("I_lehmanii228", "I_squamosum176", "I_ayabacense126","I_cyaneum170", "I_loxense101", "I_pingola105", "I_cornifolium187", 
                    "I_albi174", "I_fuchsioides154","I_calycinum229", "I_cf_loxense237", "I_cyxarb191", "I_peruvianum134", "I_tupayachianum240",
                    "E_lorentzii184", "E_Iochromoides238", "I_australe117", "E_faciculata133", "D_brachyacantha188", "I_parviflorum132", "D_obovata203", "D_spathulata136", 
                    "S_punctata178", "I_grandiflorum142", "I_umbellatum127", "I_umb_lilianum236", "I_cardenasianum135", "S_lycopersicum73" )

newnew2 <- newnew[match(OrdereredArray, newnew$NAME),]

newnew2$NAME <- as.character(newnew2$NAME)
newnew2$NAME <- factor(newnew2$NAME, levels = unique(newnew2$NAME)) 


ncol(newnew2)


datm <- melt(newnew2[,0:19])

Totaltable <- newnew2[,c(1,20)]
Totaltable[order(Totaltable$total),]


#Okay, R isn't so bad.

newnew2 <- newnew[match(OrdereredArray, newnew$NAME),]

ncol(newnew2)
colMeans(newnew2[,2:20])
newnew2[,c(1,13)]
max((newnew2[,13]))
min((newnew2[,13]))
names(newnew2)
nrow(newnew2)

View(newnew2)

newnew2[,c(1,13)]




sum(newnew2[1,2:8])
sum(newnew2[2,2:8])
sum(newnew2[3,2:8])
sum(newnew2[4,2:8])
sum(newnew2[5,2:8])
sum(newnew2[6,2:8])
sum(newnew2[7,2:8])
sum(newnew2[8,2:8])
sum(newnew2[9,2:8])
sum(newnew2[10,2:8])
sum(newnew2[11,2:8])
sum(newnew2[12,2:8])
sum(newnew2[13,2:8])
sum(newnew2[14,2:8])
sum(newnew2[15,2:8])
sum(newnew2[16,2:8])
sum(newnew2[17,2:8])
sum(newnew2[18,2:8])
sum(newnew2[19,2:8])
sum(newnew2[20,2:8])
sum(newnew2[21,2:8])
sum(newnew2[22,2:8])
sum(newnew2[23,2:8])
sum(newnew2[24,2:8])
sum(newnew2[25,2:8])
sum(newnew2[26,2:8])
sum(newnew2[27,2:8])
sum(newnew2[28,2:8])
sum(newnew[29,2:8])


ggplot(data = datm, aes(x = datm$NAME, y = datm$value, fill = datm$variable)) + 
  geom_bar(stat='identity') + coord_flip() +  ylim(0, 100) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + scale_fill_hue(c=170, l=25)+
  labs( x= "Species Name",  y ="% TE Abundance out", fill ="TE type") +  theme(axis.title.y = element_text(vjust=1.9)) + ggtitle("Tranposable Element Abundance By Genomic Proportion")
dev.off()

datm
View(newnew2)

####################################################################################
#LinearModelPrecitionRegion


NoclassI <- newnew2[,c(-2:-9)]

View(NoclassI)
NoclassI["CLASSI"] <- NA
NoclassI$CLASSI <-  rowSums(newnew2[,2:9])
NoclassI
plot(NoclassI)

ClassIsums <- rowSums(newnew2[,2:9])
View(NoclassI)

par(mfrow=c(1,2)) 


Model1 <- lm(NoclassI$total~NoclassI$LTR.Gypsy)
plot(NoclassI$total~NoclassI$LTR.Gypsy, xlab="LTR.Gypsy Abundance", ylab="Total Genomic Proportion", main ="LTR Gypsys vs Total Genomic Prop")
abline(Model1)

Model2 <- lm(NoclassI$total~NoclassI$unclass)
plot(NoclassI$total~NoclassI$unclass, xlab="Unclassifiable Abundance", ylab="Total Genomic Proportion", main ="Unclassifiable vs Total Genomic Prop")
abline(Model2)


Model3 <- lm(NoclassI$total~NoclassI$unclass + NoclassI$LTR.Gypsy)

Model4 <- lm(NoclassI$total~ NoclassI$CLASSI)
summary(Model4)

anova(Model1)



summary(Model1)
summary(Model2)
summary(Model3)
line(Model3)

NoclassI

summary(ModelTime)
abline(ModelTime)

##Below this point is code calculating the percentage of total of each type.




FnalizedPercent[,c(1,17)]
sum(FnalizedPercent[,17])/28 * 100


sum(newnew[,2:8])/28

FnalizedPercent
sum(FnalizedPercent[1,2:8])
sum(FnalizedPercent[2,2:8])
sum(FnalizedPercent[3,2:8])
sum(FnalizedPercent[4,2:8])
sum(FnalizedPercent[5,2:8])
sum(FnalizedPercent[6,2:8])
sum(FnalizedPercent[7,2:8])
sum(FnalizedPercent[8,2:8])
sum(FnalizedPercent[9,2:8])
sum(FnalizedPercent[10,2:8])
sum(FnalizedPercent[11,2:8])
sum(FnalizedPercent[12,2:8])
sum(FnalizedPercent[13,2:8])
sum(FnalizedPercent[14,2:8])
sum(FnalizedPercent[15,2:8])
sum(FnalizedPercent[16,2:8])
sum(FnalizedPercent[17,2:8])
sum(FnalizedPercent[18,2:8])
sum(FnalizedPercent[19,2:8])
sum(FnalizedPercent[20,2:8])
sum(FnalizedPercent[21,2:8])
sum(FnalizedPercent[22,2:8])
sum(FnalizedPercent[23,2:8])
sum(FnalizedPercent[24,2:8])
sum(FnalizedPercent[25,2:8])
sum(FnalizedPercent[26,2:8])
sum(FnalizedPercent[27,2:8])
sum(FnalizedPercent[28,2:8])
sum(FnalizedPercent[29,2:8])



View(FnalizedPercent)
colMeans(FnalizedPercent[,2:19]) * 100


ncol(newnew2)
newnew2
newnew2[,2:19]
newnew2[,c(1,20)]

PercentageOutofTotal <- newnew2[,2:19]/newnew2[,20]
PercentageOutofTotal
PercentageOutofTotal["NAMES"]
PercentageOutofTotal$NAMES <- newnew2[,1]

PercentageOutofTotal
PercentageOutofTotal$Namestoadd
ncol(PercentageOutofTotal)
FnalizedPercent <- PercentageOutofTotal[,c(19,1:18)]
FnalizedPercent

FnalizedPercent
names(FnalizedPercent)

FnalizedPercent[,c(1,19)]


mean(FnalizedPercent[,13])
min(FnalizedPercent[,13])
max(FnalizedPercent[,13])


mean(FnalizedPercent[,20])
min(FnalizedPercent[,20])
max(FnalizedPercent[,20])


rowsum.data.frame(FnalizedPercent[19,], FnalizedPercent)


FnalizedPercent[1,19]
mean(FnalizedPercent[,20])
min(FnalizedPercent[,20])
max(FnalizedPercent[,20])


FnalizedPercent

FnalizedPercent$NAME <- as.character(FnalizedPercent$NAME)
FnalizedPercent$NAME <- factor(FnalizedPercent$NAME, levels = unique(FnalizedPercent$NAME)) 



barplotmelt <- melt(FnalizedPercent)
attach(barplotmelt)
barplotmelt


ggplot(data = barplotmelt, aes(x = barplotmelt$NAME, y = barplotmelt$value, fill = barplotmelt$variable)) + 
  geom_bar(stat='identity') + coord_flip() +  ylim(0, 1.0001) + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) + scale_fill_hue(c=170, l=25)+
  labs( x= "Species Name",  y ="% TE Abundance out", fill ="TE type") +  theme(axis.title.y = element_text(vjust=1.9)) + ggtitle("Total Tranposable Element Abundance by Type")


rm(list = ls())
