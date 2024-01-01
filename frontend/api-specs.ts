export namespace API {
    export namespace PortfolioGetPortfolio {
        export namespace Http200 {
            export type ResponseBody = {
                average_price: number;
                current_price: number;
                frontend: string;
                initial_fill_date: string;
                max_buy: number;
                max_sell: number;
                pie_quantity: number;
                ppl: number;
                quantity: number;
                ticker: string;
            } [];
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface QueryParameters {
            user_id ? : number;
        };
    };

    export namespace PortfolioTickersGetTickers {
        export namespace Http200 {
            export type ResponseBody = string[];
        };

        export namespace Http400 {
            export type ResponseBody = {
                detail: string;
                extra ? : Record < string,
                unknown > | null | unknown[];
                status_code: number;
            };
        };

        export interface QueryParameters {
            user_id ? : number;
        };
    };
};