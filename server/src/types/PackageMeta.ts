type PrefixSymbol = string;

export interface PackageMeta {
    name: string;
    version: `${number}.${number}.${number}`;
    dependencies: {
        [name: string]: `${PrefixSymbol}${number}.${number}.${number}` | 'latest';
    };
    github: {
        username: string;
        repository: string;
    }
}