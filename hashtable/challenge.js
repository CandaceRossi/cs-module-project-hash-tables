Print out all of the strings in the following array in alphabetical order, each on a separate line.

const ballroom = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
The expected output is:
'Cha Cha'
'Foxtrot'
'Jive'
'Paso Doble'
'Rumba'
'Samba'
'Tango'
'Viennese Waltz'
'Waltz'
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible 
before writing any code.Run through the UPER problem solving framework while going through your thought process.



alph = {
    1:C,
    2:F,
    3:J,
    4:P,
    5:R,
    6:S,
    7:T,
    8:W
}

if (ballroom.includes(alph.value)) {
    poppedVar = ballroom.pop(alph.value)
    print(poppedVar)
}

