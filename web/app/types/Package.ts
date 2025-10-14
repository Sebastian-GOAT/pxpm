type PrefixSymbol = '==' | '>=' | '<=';

export type Package = {
    name: string;
    version: `${number}.${number}.${number}`;
    description: string;
    dependencies: {
        [name: string]: `${PrefixSymbol}${number}.${number}.${number}`;
    };
    github: {
        username: string;
        repository: string;
    };
};