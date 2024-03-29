


export const classNames = (cls: string = '', mods: {} = {}, additional: string[] = []): string => {

    return [
        cls,

        ...additional,

        ...Object.entries(mods)
            .filter(el => el[1] === true)
            .map(el => el[0])
    ]
        .join(' ')
}