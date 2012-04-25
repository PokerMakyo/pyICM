# It's my python version of http://pokerai.org/wiki/index.php/ICM_Equity_Calculator
#
#   /** 
#    * \param payouts Payout structure, e.g.: new double[]{0.5,0.3,0.2} 
#    * \param stacks Player stacks 
#    * \param player Index of selected player in the stack-array 
#    * \returns ICM equity for selected player 
#    */ 
#   public static  double  getEquity ( double []  payouts,  double []  stacks,  int  player )  
#   { 
#     double  total =  0 ; 
#     for  ( int  i =  0 ; i < stacks.length; i++ ) 
#       total += stacks [ i ] ; 
#     return  getEquity ( payouts, stacks.clone () , total, player,  0 ) ; 
#   } 
#
#   //Recursive method doing the actual calculation. 
#   private static  double  getEquity ( double []  payouts,  double []  stacks,  double  total,  int  player,  int  depth )  
#   { 
#     double  eq = stacks [ player ]  / total * payouts [ depth ] ; 
#
#     if ( depth +  1  < payouts.length ) 
#       for  ( int  i =  0 ; i < stacks.length; i++ )  
#         if  ( i != player && stacks [ i ]  >  0.0 ) { 
#           double  c = stacks [ i ] ; 
#           stacks [ i ]  =  0.0 ; 
#           eq += getEquity ( payouts, stacks, total - c, player, depth +  1 )  * c / total; 
#           stacks [ i ]  = c; 
#         } 
#     
#     return  eq; 
#   }

def getEquity(payouts, stacks, player):
    total = 0.0
    for s in stacks:
        total += s
    return getEquity2(payouts, stacks, total, player, 0)

def getEquity2(payouts, stacks, total, player, depth):
    eq = stacks[player] / total * payouts[depth]
    if depth + 1 < len(payouts):
        for i in xrange(0, len(stacks)):
            if i != player and stacks[i] > 0:
                c = stacks[i]
                stacks[i] = 0.0
                eq += getEquity2(payouts, stacks, total - c, player, depth + 1) * c / total
                stacks[i] = c
    return eq


te = 0.0
for i in xrange(0,5):
    e = getEquity([0.5, 0.3, 0.2], [1000, 2000, 1500, 500, 600], i)
    print e
    te+=e
print te

# vim: filetype=python syntax=python expandtab shiftwidth=4 softtabstop=4
