######################### Chapter 2 Notes ##########################

"""
Shell Expansion Tips

When working in the terminal, you can use the following:

1. '~' the tilde character tells the shell to route to the full path to your home directory ('cd ~' navigates back home)
2. '*' wildcard to expand shell to all matching files
3. brace expansion - creates strings by expanding out the comma-separated values inside the braces
    $ echo dog--{gone, bowl, bark}
    dog-gone dog-bowl dog-bark
4. range [] - goes through character/alphabet ranges specifically. try brace expansion for number ranges ({10..13})
    $ ls zmays[AB]_R1.fastq
    zmaysA_R1.fastq zmaysB_R1.fastq

Use wildcard wisely. If there are files that match but were not intended to be pulled try:
    'zmaysB*fastq' pulls all zmaysB__.fastq files
    'zmaysB_R?.fastq' pulls zmaysB fastq files with any filename R_ (zmaysB_R1.fastq, zmaysB_R2.fastq, ...)

"""
