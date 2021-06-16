import sqlite3
import sys
import os

class db:
    @staticmethod
    def get(self,table,conditions:dict):
        con = sqlite3.connect("db.db")
        cur=con.cursor()
        try:
            sql = f"selct * from {table} where"
            res = cur.execute(sql)
            cur.commit()
            return res

        except Exception:
            pass
    
    @staticmethod
    def get_words():
        con = sqlite3.connect("db.db")
        cur=con.cursor()
        try:
            sql = f"select * from words where point<=50 limit 100"
            res = cur.execute(sql)
            res = res.fetchall()
            con.commit()
            return res
        except sqlite3.Error as err:
            print("Error : "+err)
            return None
    
    @staticmethod
    def get_level():
        sql = "select sum(point) from words"
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        try:
            res = cur.execute(sql).fetchone()
            con.commit()
            return (int(res[0])//100+1,res[0])
        except sqlite3.Error:
            pass
        return (1,res[0])
    @staticmethod
    def update_words(condition:dict,fields:dict):
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        try:
            id  = list(condition.keys())[0]
            val = list(condition.values())[0]

            sql = f"UPDATE words SET "
            for field,value in fields.items():
                sql += f" {field}='{value}' , "
            sql = sql.strip(', ')
            sql += f" WHERE {id}={val}"
            res = cur.execute(sql)
            con.commit()
            return True
        except Exception:
            return False
    
    @staticmethod
    def get_user():
        sql = "select * from user"
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        try:
            res = cur.execute(sql).fetchone()
            con.commit()
            return res[1]
        except sqlite3.Error:
            pass
        return "unknow"