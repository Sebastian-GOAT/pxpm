import type { Package } from '@/types/Package';

export default defineEventHandler(event => {


    const data: Package[] = Array(12).fill(
        {
            name: 'test',
            description: 'This is a test package',
            version: '1.0.3',
            dependencies: {
                'dep1': '==1.0.0',
                'dep2': '==3.2.7',
                'dep3': '==4.6.9'
            },
            github: {
                username: 'test-user',
                repository: 'test-project'
            }
        }
    );

    return data;
});