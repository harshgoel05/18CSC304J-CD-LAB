  #include<stdio.h>  
  #include<string.h>  
  int main()  
  {  
       char gram[20],part1[20],part2[20],modifiedGram[20],newGram[20],tempGram[20];  
       int i,j=0,k=0,l=0,pos;  
       printf("Enter Production : A->");  
       gets(gram);   // input
       for(i=0;gram[i]!='|';i++,j++)  
            part1[j]=gram[i];   // divide
       part1[j]='\0';   //eol
       for(j=++i,i=0;gram[j]!='\0';j++,i++)  
            part2[i]=gram[j];   // divide
       part2[i]='\0';   //eol
       for(i=0;i<strlen(part1)||i<strlen(part2);i++)  //loop 
       {  
            if(part1[i]==part2[i])  
            {  
                 modifiedGram[k]=part1[i];  
                 k++;  
                 pos=i+1;  
            }  
       }  
       for(i=pos,j=0;part1[i]!='\0';i++,j++){  
            newGram[j]=part1[i];  
       }  
       newGram[j++]='|';  
       for(i=pos;part2[i]!='\0';i++,j++){  
            newGram[j]=part2[i];  
       }  
       modifiedGram[k]='X';  
       modifiedGram[++k]='\0';  
       newGram[j]='\0';  
       printf("\n A->%s",modifiedGram);  
       printf("\n X->%s\n",newGram);  
 }  

//   the grammar with common prefixes is transformed
//   to make it useful for Top down parsers.


// aLGO:

// We make one production for each common prefixes.
// The common prefix may be a terminal or a non-terminal or a combination of both.
// Rest of the derivation is added by new productions.