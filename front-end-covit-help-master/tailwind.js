module.exports = {
    theme: {
        gridTemplateColumns: {
            '2':'repeat(2, minmax(0, 1fr))',
            '3':'repeat(3, minmax(0, 1fr))',
            '4':'repeat(4, minmax(0, 1fr))',
            '5':'repeat(5, minmax(0, 1fr))'
        },
        colors: {
            green: '#005a9b',
            darkgreen:'#189087',
            lightgreen:'#D0E8E7',
            hover_blue:'#00365d',
            black: '#263238', //text
            black_p: '#37474f', // text description or long text
            lightGray: '#CCDEEB',
            white: '#FFFFFF',
            red: '#f67575',
            hover_red:'#C45D5D',
            orange: '#ffa34d',
            lightorange:'#FFECDB',
            gray: '#707070', // textfield
            gray_bg: '#e3e4e3',
            unHilight: '#f5f5f5',
            key_column:'#53656e',
            light_green:'#B5E1F2'
        },
        fontFamily: {
            display: ['Kanit', 'sans-serif'],
            body: ['Kanit', 'sans-serif'],
        },
        extend: {
        },
    },
    variants: {},
    plugins: []
}
