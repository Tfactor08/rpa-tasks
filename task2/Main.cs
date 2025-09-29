using System;
using System.IO;
using System.Collections.Generic;
using System.Text;
using System.Globalization;
using LTools.Scripting.Model;
using LTools.Network.Model;
using LTools.Office;
using CsvHelper;
using CsvHelper.Configuration;

public class Invoice
{
	public string Company { get; set; }
	public string Owner { get; set; }
	public string AccountDate { get; set; }
	public string RepaymentDate { get; set; }
	public string Number { get; set; }
	public string Amount { get; set; }
}

public class PrimoScript
{
	public static LTools.Scripting.CSharp.ScriptDebugger __debug;
	
	public void main(LTools.Common.Model.WorkflowData wf)
    {
		string basePath = "C:\\Users\\Tfact\\Downloads\\Telegram Desktop\\Тестовое Практика\\Тестовое Практика\\input_data\\Invoice # {0}.pdf";
		List<string> invoicePaths = new List<string>();
		List<Invoice> invoices = new List<Invoice>();
		
		for (int i = 6; i < 25; i++)
		{
			invoicePaths.Add(string.Format(basePath, i));
		}
		
		foreach (var path in invoicePaths)
		{
	        string rawPdf = LTools.Office.PdfApp.ReadText(wf, path, "", "1");
			
			string[] fields = rawPdf.Split('\n');
			
			string company        = fields[2].Trim();
			string owner          = fields[4].Trim();
			string account_date   = fields[5].Trim();
			string repayment_date = fields[6].Trim();
			string number         = fields[7].Trim();
			string amount         = fields[8].Trim();
			
			var invoice = new Invoice
			{
				company, owner, account_date, repayment_date, number, amount
			};
			
			invoices.Add(invoice);
		}
		
		string csvPath = "C:\\Users\\Tfact\\Documents\\Foo\\file.csv";
		
		using var writer = new StreamWriter(csvPath);
		using var csv = new CsvWriter(writer, CultureInfo.InvariantCulture);
		
		csv.WriteRecords(invoices);
    }
}