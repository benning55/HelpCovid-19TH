module.exports = {
    theme: {
        gridTemplateColumns: {
            '2':'repeat(2, minmax(0, 1fr))',
            '3':'repeat(3, minmax(0, 1fr))',
            '4':'repeat(4, minmax(0, 1fr))',
            '5':'repeat(5, minmax(0, 1fr))'
        },
        colors: {
            green: '#1eb2a6',
            darkgreen:'#189087',
            black: '#263238', //text
            black_p: '#37474f', // text description or long text
            lightGray: '#afbcc2',
            white: '#FFFFFF',
            red: '#f67575',
            orange: '#ffa34d',
            gray: '#707070', // textfield
            gray_bg: '#e3e4e3',
            unHilight: '#f5f5f5',
            key_column:'#53656e',
            light_green:'#d4f8e8'
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
