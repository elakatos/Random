
# Script to generate a gameboard for the classic version of the incredible game Codenames
# (https://czechgames.com/en/codenames/)
# Please don't use this script *instead* of buying the game, just as an emergency substitute/extension
#
# @Author: Eszter Lakatos

if ((require(ggplot2) & require(reshape2)) == FALSE) {
  install.packages("ggplot2"); install.packages("reshape2")
  library(gglot2); library(reshape2)
}

# Make matrix -------------------------------------------------------------
#bs = bystander (n=25), r=red (n=8 or 9), b=blue (n=8 or 9), a=assassin (n=1)

people <- rep('bs', 25)
start <- sample(c('r','b'),1) # randomly sample which team will have 9 agents
selection <- sample(1:25, 18) # randomly assign indices to the 18 'coloured' agents
people[selection[1:9]] <- start
people[selection[10:17]] <- setdiff(c('r','b'),start)
people[selection[18]] <- 'a'
people.df <- melt(matrix(people, nrow=5)) # reshape into matrix
people.df$value <- factor(people.df$value, levels=c('r', 'b', 'bs','a'))

# Plot matrix -------------------------------------------------------------

colours_cn = c('#cc2200', '#296bae', '#dfceb1', '#464646') #red, blue, bystander, assassin
ggplot(people.df, aes(x=Var1, y=Var2, fill=value)) + geom_tile(colour='black', size=2) +
  theme_bw() + theme(text=element_blank(), axis.ticks = element_blank(),
                     panel.border=element_blank(), panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     panel.background = element_rect(fill='black')) +
  guides(fill=F) +
  scale_fill_manual(values=colours_cn)

