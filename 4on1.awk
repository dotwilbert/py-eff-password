#! /usr/bin/awk -f
BEGIN {
  ctr = 0;
  total_length = 9;
  l1_1 = "";
  l2_1 = "";
  l3_1 = "";
  l1_2 = "";
  l2_2 = "";
  l3_2 = "";
  first_line = "yes";
} 

function tupleize(s)
{
  return "tuple([" s "]):";
}

function single_quote(s)
{
  return "'" s "'"
}

{
  die_tuple = gensub(/^(.)(.)(.)(.)(.)$/, "\\1,\\2,\\3,\\4,\\5", 1, $1)
  ctr = ctr + 1;
  if(ctr == 1) {
    l1_1 = tupleize(die_tuple);
    l1_2 = $2;
  } else if(ctr == 2)  {
    l2_1 = tupleize(die_tuple);
    l2_2 = $2;
  } else if(ctr == 3)  {
    l3_1 = tupleize(die_tuple);
    l3_2 = $2;
  } else {
    if(! first_line)
      print ",";
    else
      first_line = "";
    printf "%s %s", l1_1, single_quote(l1_2);
    for (c=0; c<(total_length-length(l1_2)); c++)
      printf " "
    printf ","

    printf " %s %s", l2_1, single_quote(l2_2);
    for (c=0; c<(total_length-length(l2_2)); c++)
      printf " "
    printf ","
    
    printf " %s %s", l3_1, single_quote(l3_2);
    for (c=0; c<(total_length-length(l3_2)); c++)
      printf " "
    printf ","
    
    printf " %s %s", tupleize(die_tuple), single_quote($2);
    for (c=0; c<(total_length-length($2)); c++)
      printf " "

    ctr = 0;
    l1_1 = "";
    l2_1 = "";
    l3_1 = "";
    l1_2 = "";
    l2_2 = "";
    l3_2 = "";
  }
}

END {
  lineend = ""
  if (l1_1) {
    if(! first_line)
      print ",";
    printf "%s %s", l1_1, single_quote(l1_2);
    for (c=0; c<(total_length-length(l1_2)); c++)
      printf " "
    lineend = "\n"
  }

  if (l2_1) {
    printf ","
    printf " %s %s", l2_1, single_quote(l2_2);
    for (c=0; c<(total_length-length(l2_2)); c++)
      printf " "
  }

  if (l3_1) {
    printf ","
    printf " %s %s", l3_1, single_quote(l3_2);
  }

  if (lineend)
    printf lineend
}