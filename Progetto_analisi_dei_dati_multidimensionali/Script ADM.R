Mondiali<-read.table("FIFA - 2006.csv",sep=",",header=T,row.names = 1)
class(Mondiali) <- "data.frame"
par(mfrow=c(1,1))
summary(Mondiali)
cov(Mondiali) # La matrice di varianze-covarianze
library(GGally)
cor(Dieta)
ggscatmat(Dieta, columns = 1:9)

Dieta.PCA<-princomp(Dieta,cor=F,scores=T)
summary(Dieta.PCA)
plot(Dieta.PCA,col="light blue") # Grafico a barre della variabilità spiegata
screeplot(Dieta.PCA, npcs=9, type="lines",col="blue")  # Screeplot degli autovalori

cor(Dieta, Dieta.PCA$scores)
ggcorr(cbind(Dieta, Dieta.PCA$scores), label = TRUE, cex = 2.5)

D<-Dieta.PCA$loadings  # si costruisce la matrice dei pesi
class(D) <- "matrix"
D <- data.frame(D)
print(round(D[,1:3],4))  # visualizzo i pesi delle variabili originarie sulle componenti

plot(D,xlim=c(-1,1),ylim=c(-1,1))
text(D,labels=names(Dieta),pos=4)  

PC1<-D[,1] 
PC2<-D[,2]
PC3<-D[,3]
library(scatterplot3d)
scatterplot3d(PC1,PC2,PC3,highlight.3d=T,type="h",main="Variabili nel piano dei pesi")
F1<-Dieta.PCA$scores[,1]
F2<-Dieta.PCA$scores[,2]
F3<-Dieta.PCA$scores[,3]
scatterplot3d(F1,F2,F3,highlight.3d=T,type="h",main="Unità nel piano delle componenti")

biplot(Dieta.PCA, choices = c(1,2), cex = c(.7, .7), col = c("gray", "blue"))
biplot(Dieta.PCA, choices = c(1,3), cex = c(.7, .7), col = c("gray", "blue"))
biplot(Dieta.PCA, choices = c(2,3), cex = c(.7, .7), col = c("gray", "blue"))

# dati standardizzati
Dieta1.PCA<-princomp(Dieta,cor=T,scores=T)   
summary(Dieta1.PCA) 
plot(Dieta1.PCA,col="light blue") # Grafico a barre della variabilità spiegata
screeplot(Dieta1.PCA, npcs=9, type="lines",col="blue")  # Screeplot degli autovalori

cor(Dieta, Dieta1.PCA$scores)
ggcorr(cbind(Dieta, Dieta1.PCA$scores), label = TRUE, cex = 2.5)

D1<-Dieta1.PCA$loadings  # si costruisce la matrice dei pesi
class(D1) <- "matrix"
D1 <- data.frame(D1)
print(round(D1[,1:3],4))  # visualizzo i pesi delle variabili originarie sulle componenti

plot(D1,xlim=c(-1,1),ylim=c(-1,1))
text(D1,labels=names(Dieta),pos=4)  

PC1_1<-D1[,1] 
PC2_1<-D1[,2]
PC3_1<-D1[,3]
library(scatterplot3d)
scatterplot3d(PC1_1,PC2_1,PC3_1,highlight.3d=T,type="h",main="Variabili nel piano dei pesi")
F1_1<-Dieta1.PCA$scores[,1]
F2_1<-Dieta1.PCA$scores[,2]
F3_1<-Dieta1.PCA$scores[,3]
scatterplot3d(F1_1,F2_1,F3_1,highlight.3d=T,type="h",main="Unità nel piano delle componenti")

biplot(Dieta1.PCA, choices = c(1,2), cex = c(.7, .7), col = c("gray", "blue"))
biplot(Dieta1.PCA, choices = c(1,3), cex = c(.7, .7), col = c("gray", "blue"))
biplot(Dieta1.PCA, choices = c(2,3), cex = c(.7, .7), col = c("gray", "blue"))



# ======= SCRIPT NICK ===========
PaesiKm<-read.table("PaesiKm.csv",sep=",",header=T, row.names = 1)
#print(Mondiali1)
#Mondiali <- Mondiali[,-1]
print(PaesiKm)
class(PaesiKm) <- "data.frame"
par(mfrow=c(1,1))
summary(PaesiKm)
cov(PaesiKm) # La matrice di varianze-covarianze
library(GGally)
cor(PaesiKm)
ggscatmat(PaesiKm, columns = 1:7)


# dati standardizzati
PaesiKm1.PCA<-princomp(PaesiKm,cor=T,scores=T)   
print(summary(PaesiKm1.PCA, loadings = T), cutoff = .3)
plot(PaesiKm1.PCA,col="light blue") # Grafico a barre della variabilità spiegata
screeplot(PaesiKm1.PCA, npcs=9, type="lines",col="blue")  # Screeplot degli autovalori

cor(PaesiKm, PaesiKm1.PCA$scores)
ggcorr(cbind(PaesiKm, PaesiKm1.PCA$scores), label = TRUE, cex = 2.5)

pca_sc <- data.frame(PaesiKm1.PCA$scores, country = PaesiKm1.PCA[, 1])
ggplot(pca_sc, aes(x = Comp.2, y = Comp.3, color = country)) +
  geom_point() +
  geom_text(mapping = aes(label = country), vjust=1) +
  theme(legend.position = "none") +
  ggtitle("Punteggi Comp.2 Vs Comp.3")


D1<-Mondiali1.PCA$loadings  # si costruisce la matrice dei pesi
class(D1) <- "matrix"
D1 <- data.frame(D1)
print(round(D1[,1:3],4), cutoff = .3)  # visualizzo i pesi delle variabili originarie sulle componenti

plot(D1,xlim=c(-1,1),ylim=c(-1,1))
text(D1,labels=names(Mondiali),pos=4)  

PC1_1<-D1[,1] 
PC2_1<-D1[,2]
PC3_1<-D1[,3]
library(scatterplot3d)
scatterplot3d(PC1_1,PC2_1,PC3_1,highlight.3d=T,type="h",main="Variabili nel piano dei pesi")
F1_1<-Mondiali1.PCA$scores[,1]
F2_1<-Mondiali1.PCA$scores[,2]
F3_1<-Mondiali1.PCA$scores[,3]
scatterplot3d(F1_1,F2_1,F3_1,highlight.3d=T,type="h",main="Unità nel piano delle componenti")

biplot(Mondiali1.PCA, choices = c(1,2), cex = c(.7, .7), col = c("gray", "blue"))
biplot(Mondiali1.PCA, choices = c(1,3), cex = c(.7, .7), col = c("gray", "blue"))
biplot(Mondiali1.PCA, choices = c(2,3), cex = c(.7, .7), col = c("gray", "blue"))
