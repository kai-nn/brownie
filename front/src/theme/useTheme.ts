import {useContext} from "react";
import {LOCAL_STORAGE_THEME_KEY, Theme, ThemeContext} from "./ThemeContext";

interface UseThemeResult {
    theme: Theme,
    changeTheme: () => void
}

export const useTheme = (): UseThemeResult => {

    const {theme, setTheme} = useContext(ThemeContext)

    const changeTheme = () => {
        const newTheme = theme === Theme.LIGHT ? Theme.DARK : Theme.LIGHT
        setTheme(newTheme)
        localStorage.setItem(LOCAL_STORAGE_THEME_KEY, newTheme)
    }

    return {
        theme,
        changeTheme,
    }
}